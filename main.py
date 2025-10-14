from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from azure.storage.blob import BlobServiceClient
from io import BytesIO
import os

app = FastAPI(title="Azure Blob Storage Emulator API")

# ======== CONFIGURATION ========

# Default Azurite connection string
AZURITE_CONN_STR = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

CONTAINER_NAME = "test-container"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURITE_CONN_STR)

# Ensure the container exists
try:
    blob_service_client.create_container(CONTAINER_NAME)
except Exception:
    pass  # Ignore if it already exists

container_client = blob_service_client.get_container_client(CONTAINER_NAME)


# ======== ROUTES ========

@app.get("/")
def root():
    return {"message": "Azure Blob Storage Emulator API is running!"}


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Upload a file to Azurite blob storage"""
    try:
        blob_client = container_client.get_blob_client(file.filename)
        file_data = await file.read()
        blob_client.upload_blob(file_data, overwrite=True)
        return {"message": f"File '{file.filename}' uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/list/")
def list_files():
    """List all blobs in the container"""
    try:
        blobs = [blob.name for blob in container_client.list_blobs()]
        return {"files": blobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/download/{filename}")
def download_file(filename: str):
    """Download a file from blob storage"""
    try:
        blob_client = container_client.get_blob_client(filename)
        stream = blob_client.download_blob()
        file_data = stream.readall()
        return StreamingResponse(BytesIO(file_data), media_type="application/octet-stream",
                                 headers={"Content-Disposition": f"attachment; filename={filename}"})
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {e}")


@app.delete("/delete/{filename}")
def delete_file(filename: str):
    """Delete a blob from storage"""
    try:
        blob_client = container_client.get_blob_client(filename)
        blob_client.delete_blob()
        return {"message": f"File '{filename}' deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found or already deleted: {e}")