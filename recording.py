Speaker 1

I think. [clears throat]

Speaker 2

So for example, this is the template-

Speaker 1

So basically, us is also the niche ka text bi ban jayega. Configure which data items are, uh, uh, what data is visible or exportable as shown by the default form here. Theek hai. Okay.

Speaker 2

So when you select default, it should auto-select show and export, correct?

Speaker 1

Yeah.

Speaker 2

Okay. So that's not happening for zone two.

Speaker 1

Yes, sir. We have not implemented that yet. Okay. And, uh, Naveen, as I understand, this role is for a particular department, right?

Speaker 2

Yes.

Speaker 1

So the department here should be displayed on this screen.

Speaker 2

Yes, sir.

Speaker 1

The screen doesn't say [clears throat] So now, for example, I have given a template for the staff. So I have selected a few fields. Okay. So now when I go to staff page and, uh, here also earlier this functionality I have implemented. Three equal, but because I'm an

Speaker 2

[clears throat]

Speaker 1

I, I just think very slowly. Wo default column kya karta hai?

Speaker 2

So-

Speaker 1

I understand show is for showing on the UI, export is for putting in the file. What is the default for?

Speaker 2

These are the mandatory fields. These fields always be visible in that template. So for-- on some page we want, uh, the, the list-- the fields to be default. If we land on some page, for example, on service request page or on staff page.

Speaker 1

Property will be itni dikhenge.

Speaker 2

Or the list.

Speaker 1

Hmm?

Speaker 2

List.

Speaker 1

List mein toh ye show wali dikhenge.

Speaker 2

So there is a constraint-

Speaker 1

This column is this show.

Speaker 2

Correct.

Speaker 1

Right. So what is default?

Speaker 2

So that, that is always selected for show and export.

Speaker 1

Hmm?

Speaker 2

That is always selected for show and export. So there are certain fields, right-

Speaker 1

Okay. When they want to define a custom view-

Speaker 2

Hmm.

Speaker 1

Custom template, toh itni hi dikhenge wo list.

Speaker 2

The, the, that list will have these fields pre-selected.

Speaker 1

No. So for example, if, uh, uh, an FTS user wants to define his custom view. Okay. So from the list page you have that customize, uh, custom view or the button and you define custom view. Toh mujhe woh sare dikhenge ki jo default hi unki dikhenge. For example, last name aap ne select nahi kiya hai, toh can I select last name here?

Speaker 2

Right. So we will display everything there, but whatever you select-

Speaker 1

Then, then-

Speaker 2

Default-

Speaker 1

Hang on, hang on, Naveen. Because, Naveen that, that we are getting towards inconsistencies. Uh, is this functionality of defining custom template available for, uh, non-FTS users also? For example-

Speaker 2

Yeah.

Speaker 1

A rollout center guy say that I want to see, uh, this data.

Speaker 2

Sorry?

Speaker 1

For example, can Kevin, who is not part of, uh, FTS, he's part of rollout center. When he logs into, uh, FD, uh, Bing, can he go and say, "I want to customize my view of staff," and choose what columns he wants to see? I suppose he can, right? So what columns can he choose from? Because you want to restrict him to these, right?

Speaker 2

Right. Correct. Only those we select for show and export.

Speaker 1

Export is different, Naveen. Export is what is going to go in my CSV file or Excel sheet.

Speaker 2

Hmm.

Speaker 1

I'm saying Kevin can, for example, here right now last name is not selected.

Speaker 2

Hmm.

Speaker 1

Can Kevin go and define a custom template where he selects last name?

Speaker 2

No. No.

Speaker 1

No, he can't, right? Because that is why you wanted to restrict it.

Speaker 2

Correct.

Speaker 1

Okay. So, um, so I'm still trying to figure out what is the purpose of that default column.

Speaker 2

So there are certain fields, right, that gives you the context of that, uh, data list without which you, you do not understand what data point it is, right? For example, email or the tech ID. So th-they always associate the staff with the tech ID, correct? If you see some data point in the UI without tech ID or the name, for example, they cannot relate that record to anybody or associate that record with anybody. Right? Gaurav, in the, in the next tab open that column template configuration. Keep this as is. [notification sound] So here there was a comment by Owen, right? Sometime back and, uh, Peter also. So there are certain things that should always be visible or selected, pre-selected.

Speaker 1

Yeah. You have to use it.

Speaker 2

So when you-- Correct. So when you, uh, set default there, they'll be selected in the column template something like this.

Speaker 1

Look, here I understand that these are mandatory columns in the view and export. Okay?

Speaker 2

Mm-hmm.

Speaker 1

Uh, but here, for example, you're showing last name, which I can choose to see or I can choose to not see.

Speaker 2

Right.

Speaker 1

Okay? This is fine for FPL because FPL guys have to see everything. Normally.

Speaker 2

Yes. Yes.

Speaker 1

But you may not want the same thing to happen with Kevin, who is belonging to road center.

Speaker 2

Yeah, assuming that-

Speaker 1

You may want to... Kevin, Kevin. You may want to restrict what Kevin can choose from.

Speaker 2

Right.

Speaker 1

So you may say that Kevin cannot see the address of a, of a tech. I'm assuming that for the run there'll be an address field, I guess. So you don't want him to see the tech address. Okay? But it's not even this field.

Speaker 2

In what that you said, what I'm trying to say is, for example, if you select five fields to be displayed for Kevin, right? And among this-- among those five fields, uh, admin can set the mandatory field, right?

Speaker 1

Yes.

Speaker 2

That, that... So that is what the default is meant for.

Speaker 1

Then instead of calling it default, why don't we call it mandatory?

Speaker 2

Yeah, we can change that. We can change the terminology. We can call it mandatory. Yes.

Speaker 1

It will convey much better.

Speaker 2

Yeah.

Speaker 1

Okay. Which again means that if it is mandatory, then why are you giving selection of show and export at that point? Because they're mandatory. Only non-mandatory fields you can say that I want to see or not see.

Speaker 2

Mm-hmm. So this is to just convey to user that these are mandatory fields that, that will be available for, uh, display on export.

Speaker 1

Okay. Who you have to visit, yeah?

Speaker 2

Yes.

Speaker 1

Mm-hmm. User tab mein toh nahi hai, management user hi hai tabhi. Okay. So assuming that column header is mandatory. So now here you see the inconsistency. Assuming that default template is mandatory, I have, uh, team and zone marked as mandatory, but you're saying I'm not going to show it or I'm not, not going to export it.

Speaker 2

No, because-

Speaker 1

I can change those, right? So inconsistency hai kya usmein?

Speaker 2

Because...

Speaker 1

Hmm?

Speaker 2

Because this is in progress, in progress. This is still in progress. They haven't completed that yet.

Speaker 1

Okay. But then we have this business rules defined somewhere, right?

Speaker 2

Yeah. It is different. Yes.

Speaker 1

Okay. From usability perspective, I've got a few very minor suggestions. Okay? Because if your mandatory thing is going to define or control the behavior of show and export, mandatory should be the first one. And show and export should be available for selection only when mand-mandatory is false. Otherwise, they should be by default checked in. If I say it's mandatory, then show is going to be checked, export is going to be checked. When it is non-mandatory, you can choose whether you want to show, uh, include it as a part of show, uh, and export.

Speaker 2

Right.

Speaker 1

Okay. Now I, now I have understood the functionality as well as your, uh, view. Good. Right.

Speaker 2

So the other day, I mean, people were saying that, uh, we can maintain the department list somewhere in lookup table or somewhere.

Speaker 1

Mm-hmm. I, I must not recommend equating lookup table because lookup table is user editable.

Speaker 2

Mm-hmm.

Speaker 1

Okay? And then you can't... Lookup table is, has a purpose which is used in many other places. [notification sound] Okay?

Speaker 2

Mm-hmm.

Speaker 1

But for example, we wanted to have a default template for, uh, a department, right?

Speaker 2

Mm-hmm.

Speaker 1

Where do I keep this information?

Speaker 2

The de-default template for a?

Speaker 1

For a department. When I define a... Okay, so Kevin may, uh, Peter may say, "I don't want the, uh, uh, road center to see a set of fields." Okay?
 


Speaker 2

Mm-hmm.

Speaker 1

Where do I define that? Only in the role?

Speaker 2

Yes.

Speaker 1

And that department can have multiple roles, so you have to remember what is the, my limit of what I can assign to the role.

Speaker 2

Yeah.

Speaker 1

And if he doesn't assign any roles to the user, what happens? What does he see?

Speaker 2

He gets to see a de... He gets, he gets to see a default view where he can only see site information page where it says, you know, the site, uh, name, georeferenced electrical network. And the Peter wants to display that in the map also, just the map. Only the site location on the map, no other controls on the map.

Speaker 1

So let's go over my, uh, question again. Uh, if I define a user for road center. Okay? So I selected department as road center, and, uh, I don't assign him any ro-- any, uh, roles.

Speaker 2

Mm-hmm.

Speaker 1

Okay? Now this guy logs in, he goes to the site list. What will be the restrictions on him? What can he see? What he cannot see? What can he, uh, put in the show list or export list? You can try creating a user like that, right?

Speaker 2

You can try creating a user like that, but that is not implemented yet. But the requirement is such, uh, Rahul, open that next tab and go to site information page. So when-- Assuming that Kevin is created as a new user and he's not assigned with any role but have to work for so and so department. So he's just to get to this page, site information page. There on the left-hand side, he can see this list, the site list, right? On the right-hand side, the content body, he won't see anything. He'll not even see anything there. He'll just see the location. Open location tab. Okay? So we don't even show the location tab. We'll just display the map with the location of the site. That is what, that is what he wants. So no other, uh, data point that he will be able to... So all these controls on the map will also go.

Speaker 1

Just a minute. Yes.[coughing] Naveen, you know what the office is. [coughing] Just a minute, let me have a glass of water. So Kevin logged in and he did here, and then we are saying that he's going to see only a set of quantity fields. Right? Because those are the site list. So where is that list coming from?

Speaker 2

You'll just see the list, uh, from the left-hand side, the site list.

Speaker 1

That's right. Yeah.

Speaker 2

Site will be added. Only the map.

Speaker 3

Map location. Or map may be selected site ID or location.

Speaker 2

Only selected site location. No location.

Speaker 1

No, but this will be added here.

Speaker 2

Nothing. We'll just show the map on the right-hand side.

Speaker 3

That's it.

Speaker 2

Not a location.

Speaker 3

If any user has no assigned any role, in that case only show the left-hand side list and the right-hand, uh, field map. Only map without any filters, without any-- only selected site in the map.

Speaker 1

Map will be empty.

Speaker 3

No. Filters will be.

Speaker 1

No filters.

Speaker 3

The map filters will be.

Speaker 1

Yes.

Speaker 3

Um, but sir, do you doubt that it will be assigned? Suppose I assign a role as technician. There is an FPS user whose role is as technician, Adam. This Adam has a service request. So, uh, in the service request, what did I do? What did his manager or admin do for the technician? Suppose five-- first five properties, fields. He marked show as default and Adam logged into his application. He went to the service request page. He saw five fields, site service request and service variety. Then when we open the column definition-

Speaker 1

Naveen, are you able to follow? Or you want her to speak English? Sorry.

Speaker 3

Uh, in service request column definition-

Speaker 1

Mm-hmm.

Speaker 3

-only these, uh, five fields are visible or other fields?

Speaker 1

That is my question. What will be shown in this?

Speaker 3

Or if only five are shown, then there is no point in the column definition.

Speaker 1

That is exactly what I am taking away. That behavior is to ensure consistency. So if, if I have to visualize, I say, "Okay, I define a department and I define its scope." What can the staff see in this department?

Speaker 3

Data control.

Speaker 1

Okay. Uh, staff gets that list that there are no limits beyond this. Okay. We can see less in this, but we can't go beyond this. So that is why I'm saying that we need to have this definition that I'm not saying this is where we can't move beyond what we implemented so far. So if, if when I define a department, I also say this department people can see because it takes in the staff. Yeah, when you things in the van and so on, right? This is what we define. And when I define a role, I can choose from this list. I can't go beyond this. Okay. Because I said that we can see twenty-five people in this department. We can't go beyond those twenty-five. Out of those twenty-five, two people can only see ten. Okay. Now when that person logs in and wants to define in his custom table, he can choose from these ten because he only has access to these ten. Out of that, he can say that he doesn't want four.

Speaker 2

Sir, the department info is different.

Speaker 1

Department is setting the scope.

Speaker 2

Yes.

Speaker 1

This is my upper limit.

Speaker 2

Yes. We have to set the department somewhere.

Speaker 1

Yes.

Speaker 2

That's what you are saying.

Speaker 1

So the department... That's why I say that lookup list should be given to me because the purpose of the lookup list is different. You are using more things than that. You put the department in it. So the additional things that are required cannot come in. That is my, that is why my comment in the chat box, the department should become a proper class to which you say that it has these limits. And as soon as that limit comes, I define its role accordingly. It will run on the same limit. The user comes, it will run on the same limit. The user gets another restriction that his table is limited according to that. Uh, Naveen, one question.

Speaker 2

Yeah.

Speaker 1

Is this mandatoriness dependent on the user or it is dependent on the data, on the resource?

Speaker 2

Which one?

Speaker 1

See, for example, saying, I'm saying in the site view you need to have, uh, site and tech ID and all that, right? In this service request. In service request, I need to have site service request ID, incident ID, CID. These are my mandatory things.

Speaker 2

Mm-hmm.

Speaker 1

Is this mandatoriness attribute of service request or of a particular role or a user?

Speaker 2

So this is of a particular role and the data template.

Speaker 1

So for a different role, I may have different mandatory fields.

Speaker 2

Correct. Right. Right.

Speaker 1

Okay.

Speaker 2

So we can-- The only difference from your vision is that, uh, yes, you wanted a definitive class of the table, right, for department, but we are using lookup groups here. So the reason being lookup groups are handy and, and, uh, I mean, you can create a lookup group item without depending on this as and when it is required. But when we, uh, do the same thing with the department, we need to provide an interface where we can-

Speaker 1

I know. It's more work. I understand that. Lookup was already available, so you utilized it. But, uh, even if it is more work, I think, uh, having it as a first-class citizen will help. As usual, let me use the board to convey what I'm trying to say.

Speaker 2

Okay.

Speaker 1

And again, one minor thing. Let me share the screen.

Speaker 2

Yeah.

Speaker 1

Let me know whether you can see the screen. Are you able to?

Speaker 3

Yes.

Speaker 2

Yeah, we can see.

Speaker 1

Okay. So I'm putting my thoughts. It's not a spec, so we'll, we're putting these thoughts for review. I have a department. Mm-hmm. Okay. I define the data scope for that. I have this set of fields. Okay? Some set of fields that any person of this department can see only this data in the staff. Okay? Then I got roles of that department where I say I have a subset of data. From within this, he-- the, the role cannot go beyond what is defined for the department. Okay? Now I got user. Okay? So user has a role, so accordingly, he gets access to that data, but he can define a custom table, right? Now, from what you guys are saying or what I understood from what you guys specifying, this user also needs to have a restriction. First restriction is department is setting a limit. He cannot go beyond the limit set for the department. Can we go beyond the limit set for the role? No. Okay. So we-- then our spec at the role level is slightly incomplete. I'll tell you why. In your role, you had show, you had export, okay, you had mandatory. Okay? You are saying that the set of fields are mandatory from which I want to show something, I want to export something. But for example, my... Okay? My department level list was so long. Okay? Department list. But my mandatory list was only this much. These are mandatory, so, uh, these are object. User cannot change these because they're mandatory. Okay? These are the fields which are optional, but optional only for display or for user. So I can say accessible. Okay? So... And you must have seen this new term, which I will explain shortly. Accessible. What are the-- This is my data scope. What are the fields which are accessible to a user of this sc-- this, uh, role is a bigger list. Okay? Of which these are mandatory, and this is what by default you're going to show or allow export. Now, when user says I want to define a custom template, he is restricted to this. What is accessibility?

Speaker 2

Okay.

Speaker 1

Okay. It will cover all the mandatory. It will cover what he's right now able to see, but he can go beyond and have extra. [coughing] Naveen, are you with us?

Speaker 2

Yeah, but, uh, okay.

Speaker 1

Then I'm very consistent. I'm saying any person of a department, I'm saying what he can see. Okay? Within that, a particular role guy can see a smaller subset of which even a smaller subset is mandatory or mandatoriness can be defined here. Okay? Because whatever is mandatory is mandatory, whether it's accessible to me or not. Okay? Because without that, the data is incomplete. Effectively, what is mandatory is without this, the data won't make sense. Okay. So I can have a flag here which says mandatory. Okay? So I got whatever thirty fields here, of which five are mandatory, so that part is handled. I say within these thirty fields, these twenty-five fields are accessible to this role. And by default, I'm going to show whatever I did that show. Naveen, comments.

Speaker 2

How, how is this different from show export?

Speaker 1

Hmm?

Speaker 2

The existing.

Speaker 1

Yeah. So now, the moment you create a user, okay, and user for a department, he will see what is mandatory within his role. These were mandatory: F one, F two, FH. Okay? So these are mandatory, so he will see only these because no role was assigned. Okay? The moment you assign role, then you know what to show. Naveen? Hmm? Thoughts, comments.

Speaker 3

Uh, sir.

Speaker 1

Sorry.

Speaker 2

No, I didn't completely understand this. Means you saying, uh, you're separating it-- separating mandatory list and the accessible list.

Speaker 1

Correct. Anything which is mandatory is accessible because you are saying it is mandatory.

Speaker 2

Mm-hmm.

Speaker 1

If it was mandatory, then why are you not letting me see it? That would be inconsistent, right?

Speaker 2

Sorry, sorry. Can you please repeat that?

Speaker 1

I'm saying that if something was mandatory and you say don't see it, then it is inconsistent.

Speaker 2

No, we are not saying that.

Speaker 1

Yeah. So with this model-

Speaker 2

This one is never mandatory.

Speaker 1

With this model-

Speaker 2

Mm-hmm.

Speaker 1

-that accident will never happen.

Speaker 2

I did not understand.

Speaker 1

Okay, let me walk through the whole process again. Okay? Let's say my staff has F one to F fifty. Okay? Fifty attributes. I define a department, role of sender. I say of these fifty fields, these thirty fields are department scope. So any person of this department cannot see beyond these thirty fields. Are we in sync on that? Naveen? Don't worry about the accessibility part. Just right now, focus on the department scope.

Speaker 2

Yes.

Speaker 1

Okay. Of those thirty fields, these ten fields are mandatory or five fields are mandatory. Are we okay with that? So now any user of this department will be able to see these five fields, whether he has been given a role or not.

Speaker 2

Okay. Through the role you are saying.

Speaker 1

Yeah. We-- You don't have to assign a role. We are saying you are part of this department, so you will see these mandatory fields, and you can view them, you can export them, you do whatever you want. Okay?

Speaker 2

Okay.

Speaker 1

Now, for a particular role, you may say, "Okay, uh, the department has scope of thirty fields, but for this particular user of this department, I want to restrict him from F one to F twenty. Last ten fields I don't want him to see ever."

Speaker 2

Mm-hmm.

Speaker 1

Okay. So now when he wants to define his custom template, he is restricted to F one to F twenty. He can't go beyond that because his role doesn't allow him to.

Speaker 2

Mm-hmm.

Speaker 1

Okay.

Speaker 2

Okay.

Speaker 1

Along with that, so mandatory is one from here, it has one in the requirement. Okay, so we don't need it here. I say in this role, by default, show me from F one to F fifty. Okay? Or if then any export I want from F one to F fifty. Right. So now, the moment you assign this role to a user, when he goes to staff list, he is going to see department F10. If he exports, he is going to get department F10.

Speaker 2

So we are doing a two-step process here. One is each department we are defining the fields, the mandatory fields.

Speaker 1

Yeah.

Speaker 2

And additionally, if he is-- if he wants him to access additional fields, we define, uh, roles for him.

Speaker 1

So at role level, you are not defining mandatory fields across it and across the code. Okay?

Speaker 2

Yeah.

Speaker 1

[अस्पष्ट संवाद] So at role level, I only say show and export because my mandatory list is already defined.

Speaker 3

Sir, एक minute.

Speaker 1

Okay.

Speaker 3

Role का page share कर दें। आप वहाँ पे बताओगे।

Speaker 1

Don't share.

Speaker 3

Okay.

Speaker 1

Can you show me the screen?

Speaker 3

Yes.

Speaker 1

The screen.

Speaker 3

Yes.

Speaker 1

Which I-

Speaker 3

[अस्पष्ट संवाद] Sir, ये, ये role है IT technician. इसका department है FPS. इसके लिए वो department tag accessible field or show is एक default deposit.

Speaker 1

जब आप staff management को खोलोगे ना, तो आपको department की list दिखेगी। That will be only accessible list. क्योंकि बाकी तो उसको accessible ही नहीं है ना। Sorry, sorry. My bad. ये जो रहेगी वो department scope की list रहेगी और यहाँ पे एक column आ जाएगा accessible. Okay. Mandatory नहीं है। यह column नहीं है क्योंकि mandatory ने सब हमने department में define कर दिया है। Right? So accessible में जो-जो mandatory और non-mandatory हैं, you can't change that क्योंकि वो हमेशा ही accessible चाहिए मुझे। Okay. उनके आगे का show or export भी tick रहेगा। जो non-mandatory field है पर department scope में है, वहाँ आप ये बोलोगे कि इस role को वो accessible है क्या। So RFD, RFD department है ना। हाँ, तो RFD department में managing role है and technician role है। Manager को ज्यादा data दिखता है, technician को कम दिखता है। तो manager role define करोगे तो आप accessibility column में additional fields को tick कर दोगे। Mandatory थी, additional वो आप tick कर देंगे कि इनके RFD के manager को ये चार चीजें और दिख सकती हैं या ये 10 चीजें और दिख सकती हैं। Okay. उनमें से ठीक है कि कौन सी हैं वो show or export में हैं। जो नहीं दिख सकती उसको show or export की बात ही नहीं आती क्योंकि वो accessible ही नहीं है।
 


Speaker 3

तो sir, accessible जो है वो किस purpose से है? मतलब for example कि, यहाँ पर हम accessible की जगह if show export करेंगे तो उसको manage कर सकते हैं।

Speaker 1

नहीं, नहीं। ये show होगी कि by default ये role ले को उसको क्या दिखेगा। मैं, मेरे को-- आप RFD का manager हो। आपने बोला कि ये 10 field आपको दिख सकती हैं। पर मैं customize करके और भी चीजें देख सकता हूँ।

Speaker 3

अच्छा! तो वो custom के लिए accessible है।

Speaker 1

वो custom के लिए accessible होगी this way. मेरे को custom template बनानी है तो उसकी limit लगानी पड़ेगी।

Speaker 3

Sir, तो यहाँ से अगर मैंने show select नहीं की, accessible select किया then मुझे customize नहीं किया।

Speaker 1

मैं show तभी select कर सकता हूँ जब accessible select है। यानी मैंने accessible नहीं select किया तो show का सामान ही नहीं आता है।

Speaker 3

Show is for table.

Speaker 1

Show is for default view for this role. Effectively, I am defining the default view for that role. And then I can create a custom template which is based on what is accessible to.

Speaker 3

Okay.

Speaker 1

Clear?

Speaker 3

हाँ, एक बार आपको जैसे-

Speaker 1

Now put a scenario. We'll go through that.

Speaker 3

अभी एक technician है, FPS का handler है वो। जहाँ पे service request में हमने five, उसको 10 भी कह रहे bind करके। Service request में 10 properties हैं। इसमें से accessible हैं उसको पांच। उसमें और उसमें show और export में तीन things लिख के आया। जब वो technician login करेगा, service request के page पे जाएगा तो उसको by default show के हिसाब से दिखेगा और उसके column template का जो definition है उसमें से पांच column読ेगे। बाकी का तो accessible है लेकिन-

Speaker 1

Accessible है लेकिन-

Speaker 3

उसमें नहीं दिखेगा।

Speaker 1

बाकी कुछ नहीं दिखेगा।

Speaker 3

ये एक first case clear हो गया। दूसरा suppose मैंने accessible में भी five properties लिख के हैं, same properties show में भी select किया, same properties export में भी select किया।

Speaker 1

ठीक है।

Speaker 3

तो उस case में column template नहीं दिखेगा।

Speaker 1

क्यों? मेरे को export कम करना है, मुझे कम देखना है। My data points हैं। I will reduce what you are showing me by default.

Speaker 3

Okay.

Speaker 1

Custom templates हमें इसलिए नहीं दिखाते हैं अपन, allow करते हैं कि मुझे ज्यादा देखना है। मुझे कम देखना है कभी होता है। मेरे काम की नहीं है ये जो तुम मेरे को दिखा रहे हो, मेरे काम की नहीं है। So I don't check it.

Speaker 3

Okay. तो suppose मैंने service request के लिए वो देख किया कि पांच fields थे, उसमें से मैंने export के दो देख लिए थे उसमें।

Speaker 1

हाँ।

Speaker 2

But sir, if those five fields are mandatory.

Speaker 1

क्या?

Speaker 2

Sir, कि मैंने की थी first field है accessible मुझे।

Speaker 1

मुझे मराठी नहीं आती है। हिंदी में वो field कौन कैसे बताएगा?

Speaker 2

Under accessible we have five fields.

Speaker 1

हाँ।

Speaker 2

And that five fields are mandatory.

Speaker 1

Correct.

Speaker 2

And that is checked in show as well as in export.

Speaker 1

Correct.

Speaker 2

So-

Speaker 1

And the remaining are unchecked. वो-

Speaker 2

हाँ।

Speaker 1

Disabled.

Speaker 2

So what you are saying then what is the need of that column template?

Speaker 1

हम्म?

Speaker 2

Then what is the need of that column template?

Speaker 1

Column template मैंने अभी जैसे बोला ना, अभी आपके पांचों mandatory और आपके scope में, uh, आज accessible scope में पांच field में कुछ नहीं है। तो you really cannot customize.

Speaker 2

हाँ।

Speaker 1

That is true. Okay. तो मान लो आपकी accessible list में 10 हो गई। तब क्या करते? तब आप customize कर सकते हैं, तब आएगा।

Speaker 2

अगर ये सही है वो तो फिर column template-

Speaker 1

You can choose to show it but you can really not do anything on that dialog. Right? क्योंकि उसको uncheck करने के लिए या check करने के लिए कुछ नहीं बचा है। पूरा UI disabled है तो even if you bring that UI, it doesn't help you anyway. आपको काम बढ़ा के बोलना है कि ये मेरे पास कुछ नहीं है accessible में extra तो मैं कोई UI नहीं दिखाऊंगा। It's your call. दिखा देने से कोई नुकसान नहीं होने वाला है।

Speaker 3

तो एक बार आप staff के बाजू में accessible column लिख दो और default को mandatory में-

Speaker 1

Sorry, you won't be able to see this because I am writing as a normal user. Okay? But for their help, I am writing. Okay? ये accessible है पर आपने select नहीं किया है। ठीक है? उसमें से मैं बोलता हूँ कि ये जो चार हैं, ये mandatory हैं। Okay? वो मैंने department level से ही mandatory हो के आएंगे तो आपका हम change नहीं किया, वो तो आएंगे ही। वैसे ही ये भी, ये सारी की सारी disabled रही। ये तो पता नहीं है आपको। ये जो रहेगी, ये disabled रहेगी। क्यों? क्योंकि ये mandatory है। नीचे ये तीन choice हैं आपकी। आपने उसको accessible कर दिया तो आपको ये check uncheck करते रहेगा। मान लो कि मैंने इसको नहीं check किया तो मुझे इनकी state नहीं change करते है क्योंकि ये मेरे को accessible ही नहीं। तो show export की बात ही नहीं आती। मेरे को accessible ही नहीं।

Speaker 3

तो अभी हमने जैसे कहा कि ये जो accessible है वो, वो समझो 50 property है वो mandatory है। जो department से है।

Speaker 1

Department level पे हमने बोला था कि ये staff का ये data जो है mandatory है pure access में।

Speaker 3

यानी हमें नया page बनाना पड़ेगा department.

Speaker 1

Department definition में आपको करना पड़ेगा जहां पे काफी सारा काम है। Okay.

Speaker 3

एक बार department tab का भी design कर दो।

Speaker 1

तो हमें वो इसी कहानी से बाद। ये बंद कर दो ना।

Speaker 3

हाँ।

Speaker 1

This में नहीं आ गया।

Speaker 3

Yes.

Speaker 1

हाँ बंद कर दो।

Speaker 2

We are essentially doing the same thing.

Speaker 3

accessible वाला mandatory।

Speaker 1

Accessible वाला disabled कर दो। ये तीनों disabled कर दिए और ठीक हो गए।

Speaker 2

Naveen is saying something.

Speaker 1

हम्म?

Speaker 2

Yes, Naveen.

Speaker 1

Yeah, Naveen.

Speaker 2

We are essentially doing the same thing but in two step process.

Speaker 1

Correct. Okay, now let me go back to one view that she wants to see. Okay. So, okay, let me share the screen because Naveen won't be able to see that. Now tell me whether you can see the screen.

Speaker 2

Yeah, I can see now.

Speaker 1

Okay. So... वही अपना role का URL वैसे ही आएगा। इसको मैं ये checkbox में convert कर देता हूँ। [घंटी की आवाज़] यहाँ मेरी property based property, my little accessible. Okay. I am saying ये जो मेरे role में ये 15 हैं, उनमें से मुझे कौन सी इस department को access देनी है। को accessibility देनी है। और उनमें से कौन सी mandatory है। Okay. Naveen, are we in sync?

Speaker 2

Yeah.

Speaker 1

अरे ये save कर लेंगे इस time PDF में। [खाँसने की आवाज़] So I define a department. I say कि वो department का data access का scope क्या है? उनमें से mandatory क्या दिखाना है मुझे। ये हो गया कि फिर मैं अपने role के URL दे देता हूँ। वहां role को एक department assign कर देता हूँ। जैसे ही department assign करता हूँ this tells me कि वो क्या access कर सकता है। Mandatory भी बता देता है कि ये चीजें उसमें से mandatory है। बचे हुए जो हैं उसमें जब वो बोलता है कि इस role को ये field to access देना है then you can ask a question कि मुझे दिखाना है कि नहीं दिखाना है। Export में देना है कि नहीं देना। जो unchecked है उसके आगे show export disabled or unchecked रहेगा। ठीक है।

Speaker 3

ठीक।

Speaker 1

Straightforward है logic अब।

Speaker 3

Yes.

Speaker 1

मुझे लगता है client server side पे। Because using all this logic when you are emitting the data you have to restrict the data to this. वो लाख बोले कि उसका क्या है। तुमने data देना ही नहीं है उसे इनका। ठीक है। So even if she accidentally shows some column with some property which are not accessible it will be all blank. Question, question.

Speaker 3

अभी one minute, one minute.

Speaker 2

Can I ask you a question? Hello.

Speaker 1

Yeah.

Speaker 2

So what flexibility or externality achieve with this?

Speaker 1

Sorry.

Speaker 2

So what action, flexibility or benefit that we get with this?

Speaker 1

We will be very consistent about what a department person can see independent of his role, assigned or not assigned. Because you are saying that this department guys can have access only up to this data. Whatever be their role.

Speaker 2

So that gives a client experience to, I mean, when they are asking any role.

Speaker 1

I don't think I understood your question.

Speaker 2

When you are saying that the department, all department users will have client experience for what they see in export when they do not have any additional role.

Speaker 1

They can have an additional role within them.

Speaker 2

No.

Speaker 1

Okay. For example-

Speaker 2

They have an internal role but when they do not have any role.

Speaker 1

Then automatically they are restricted to what is mandatory.

Speaker 2

Okay. So can we merge this one into that role thing or we keep them separate? Because-- so this one makes them to define the departments first and then go to roles again and they don't have any access.

Speaker 1

Again, let's, let's be, uh, more consistent on the terminology. At department level, we are primarily defining accessibility. What data can be accessed by persons of a department. Okay.

Speaker 2

Okay.

Speaker 1

Some of those are marked as mandatory. Unless the data is accessible, mandatoriness has no meaning. So I define that these 20 fields are accessible to users of IT. Okay. Of these, these five are mandatory. Okay. Hello? [घंटी की आवाज़] [घंटी की आवाज़] [घंटी की आवाज़] [घंटी की आवाज़] Hello, Naveen, can you hear us?

Speaker 2

Hello, [अस्पष्ट संवाद]।

Speaker 1

Okay. Yeah, there was a breaking in between. So once you have defined the accessibility scope, access scope for data, then within that the department guy may say my manager should be able to see these, uh, 15 fields and my tech should be able to see only these 10 fields. So that will be controlled by the role.

Speaker 2

[खाँसने की आवाज़]

Speaker 1

If you don't do this, if you don't do this, then Peter has to remember that for this particular department, I need to restrict the access to this. First thing, there is no restriction. Right now you have nothing which is saying what is restricted for the department. The moment he finds a custom template, he has access to everything.

Speaker 2

No, he still has a restriction.

Speaker 1

Where?

Speaker 2

We are going to implement that way. Sorry?

Speaker 1

Your present UI didn't show me how you are restricting to a certain set of fields. You are saying by default you can export these, but you are not restricting access to other fields.

Speaker 2

No, this is a single implementer part.

Speaker 1

Okay. Okay.

Speaker 2

We are seeing the definition part.

Speaker 1

Hmm.

Speaker 2

Defining the role and, uh, the requirement field set. We are still not implemented that later part.

Speaker 1

So where were you going to store the accessibility part? In the role definition itself?

Speaker 2

In the role definition itself.

Speaker 1

Okay. But then Peter, we have to be very consistent that he ensures that, uh-

Speaker 2

He says we are making two bookings every day for the-- for all those. That's the extra work that he has to do. You know?

Speaker 1

Yeah, I see.

Speaker 2

Yeah.

Speaker 1

But there are other administrative works also. For example, if the later they negotiate and say, uh, RFT says that, "Hey, I need access to that data also," then we have to go and make change in all the roles of that RFT.

Speaker 2

Okay. But that's what I'm saying. Uh, the bare minimum thing, the bare minimum thing across all roles within the department-

Speaker 1

No, no, no, no. No, no. I'm not talking of mandatory. I am saying that RFT says that I optionally need access to this particular attribute also. So I'm not saying that this way is mandatory, but I'm saying I need access. I should be able to choose and say, "Okay, I want to see this," for example, data of the staff for whatever reason they want access. How can you do that across the roles in one go? Here it's very simple. Go to the report department definition, uh, in the accessibility, just check in front of DOB and it's accessible to all the staff.

Speaker 2

Okay. That is the only thing missing. Yeah. That's the, that's the-- That is what is missing. So otherwise, uh, it is pretty much the same.

Speaker 1

Yeah. Principally, this is access control, data access control.

Speaker 2

Right.

Speaker 1

Yeah.

Speaker 2

Right.

Speaker 1

Yeah.

Speaker 2

Yeah. So, uh, yeah. So we are going to get two user interfaces. One is where they define a department and the-

Speaker 1

The role-based role, uh, definition has some changes.

Speaker 2

Right.

Speaker 1

Yeah.

Speaker 2

So we need to define two screens. Can we do that? So one is for the department, which you are already, which you are already presenting now, and that's why I can see that in the board.

Speaker 1

Mm-hmm.

Speaker 2

And the second one is, uh, how to associate additional fields for a new role for the department.

Speaker 1

It's automatically happening because of this. Oh, okay, I got your point. I got your point. Sorry, I missed that. Uh, what he's saying is that department has access to, uh, one to twenty. Okay. But for a role, he wants to restrict it to one to fifteen. Okay. So when a user of this role comes and says, "I want to define a custom template," it should be one to fifteen, not one to twenty, which is the permission for the department. Right, Navin?

Speaker 2

Yeah.

Speaker 1

Yeah. So, uh... Yeah. So similar accessibility part will be there in, uh, that also. Okay. So this-- That UI will also be very similar to, uh, what we are doing for role. Okay. Staff. The list here is automatically defined by department accessible. Accessible attribute properties. Okay? This list will only be that much. Even if your staff has fifty fields, this is the list, listing only thirty. Okay. Then he's saying accessible. Which are the fields that are accessible to this particular role? Okay? Then what-- Which are the ones we want to show and which are the ones we want to expose by default? So I will have thirty, F1 to F30. I have these thirty, F1 mandatory. Then you will mark which are accessible, and only those you can use for selection. So there can be something which is accessible but not shown by default or exposed by default.

Speaker 2

So for example, in department definition for, uh, staff, we have fifty fields.

Speaker 1

We have fifty fields. Okay.

Speaker 2

Okay. From that, we have given thirty fields as accessible.

Speaker 1

To that department.

Speaker 2

To that department.

Speaker 1

Uh.

Speaker 2

Thirty as accessible, then fifteen as mandatory.

Speaker 1

Mm-hmm.

Speaker 2

So here, by defining a role, we will get that thirty fields.

Speaker 1

Only thirty.

Speaker 2

Thirty fields.

Speaker 1

Even though staff had fifty, here I'm listing only thirty.

Speaker 2

And from this thirty, we'll again mark accessible.

Speaker 1

We'll again mark which fields are accessible to this particular role.

Speaker 2

Okay. For role.

Speaker 1

For role. This I am doing a role definition, right? So that will be a subset of these thirty. Of those mandatories are anyway, they're just, um, getting carried forward. So of those thirty, you mark only ten as accessible. So when a user of this role tries to customize, he's not looking at thirty, he's looking at F30.

Speaker 2

Okay.

Speaker 4

So, sir, why not we, you know, only auto-select this accessible list-

Speaker 1

Mm-hmm.

Speaker 4

With that, uh, department list. So

Speaker 1

No, no, no. Department main, uh, let's take manager here example. Okay. Manager ko tees main tees field accessible hai. Toh staff ko woh dekhenge easy hai.

Speaker 4

Agar hum isko pura try karein toh ek, ek mark karne mein, agar kam karna hai toh kam karna easy ho jayega na agar woh already selected ho ke aata hai.

Speaker 1

Woh default UI kya karti hai, woh iske aap.

Speaker 4

Agar ye accessible list mujhe auto, auto select ho gayi immediately toh main waise hi on editable.

Speaker 1

Toh mujhe isko inaccessible karne ko ho raha hai?

Speaker 4

Nahi, nahi, nahi. Main ye bol rahi hoon ki jaise ki ye role wala page matlab aayega. Ye F1 to F30 fields wali woh department define thi, woh accessible jo bhi fields thi woh yahan aayegi aur woh auto select ho jayegi.

Speaker 1

Aur user ko kya karna hai?

Speaker 4

User ko hai, woh select kar sakta hai.

Speaker 1

Woh, woh new role banate hi mujhe chahiye ki woh full check karke de sakta hai.

Speaker 4

Haan. Kyunki select karna thoda tough ho jayega mujhe agar jyada fields usko denge.

Speaker 1

Agar check karke denge toh mujhe ye karna ka meaning hi nahi hai. Ye toh mere depends ki aapka scope requirement kya hai. Mujhe tees main se pandrah field lana hai toh mujhe dono taraf check karna hai.

Speaker 4

Haan, woh toh-

Speaker 1

Tees main se pandrah check karna hai.

Speaker 4

Par practically mujhe aisa lagta hai ki, uh, kam karna hi agar user wahi keh raha hai toh hum isko kam hi karenge.

Speaker 1

Yeah.

Speaker 4

[chuckles] Aur, aur ye show aur expose ko kabhi editable-

Speaker 1

But no. Normally, corporations are a department bureaucratic hai. So they don't want to give access. Don't want to give access, right? Which means main default check karna chahiye. [chuckles]

Speaker 4

Aur ye show and expose jab accessible bana hoga tabhi-

Speaker 1

Tabhi woh available hoga, right? Kyunki accessible hi nahi hai toh show hi kyu karna chahiye.

Speaker 4

Aur mandatory hai jo kya aap-

Speaker 1

Mandatory hai toh woh anyway check karega.

Speaker 4

Toh ye toh, ye toh jaayega dono mein.

Speaker 3

Navin, I have a question.

Speaker 2

Yes.

Speaker 3

Uh, what Peter actually wants. He want, uh, total flexibility for manual selection or, uh, he want that mandatory section also?

Speaker 2

So mandatory section is something we are defining as a bare minimum, uh, fields that everybody can access in every department Each department will have multiple roles, right?

Speaker 1

Right.

Speaker 2

So like when say a lower, lower level role or a high level role.

Speaker 1

Mm-hmm.

Speaker 2

So lower level role is something that you, uh, don't have to define, right? So he gets to see all his, uh, accessible fields that we defined at the time of, uh, department definition, right?

Speaker 1

Okay.

Speaker 2

And then a, a higher level role would, would, would be able to see additional things. So that is when you create a new role. And in addition to this default level accessible fields, you also select extra columns or fields location.

Speaker 1

Mandatory is mandatory for all roles, HR.

Speaker 2

Correct. Mandatory for all roles. So can you, uh, keep the selection in one place for convenience? So I don't want to manage the department page again.

Speaker 1

Hmm? I don't want to?

Speaker 2

Manage department page. For example, uh, okay. So for example, like you said, if someone wants to-- if someone is requesting for an additional field.

Speaker 1

Mm-hmm.

Speaker 2

Right? Uh, so he has to go to the manage department page and select that field, correct?

Speaker 1

Correct.

Speaker 2

So can we keep that ma-department definition and, uh, role level, uh, consideration at one place for convenience?

Speaker 1

It can happen. People holds in a department, right? So you cannot remove the department, uh, role page. [coughs]

Speaker 2

Mm-hmm. Correct.

Speaker 1

[coughs] Sorry.

Speaker 3

Sir, to manage department main, uh, jo abhi jo, uh, data the humne-

Speaker 1

Vikram, yeah, Vikram, can we please...

Speaker 2

Sorry? Can, can we do this instead?

Speaker 1

Mm-hmm. Mm-hmm.

Speaker 2

We create one of the default role, a system default role, which is not editable, meaning, uh, not editable by everybody, but he can edit it. Okay. That stays as a default role for all the departments. Meaning every department will have its own role, default role, okay? Where he selects whatever accessible column he wants, right? And, uh, here in the roles definition page. So that is how to check all this.

Speaker 1

No, but this is automatically happening, Naveen. When I define a, an accessibility scope for a department, effectively, I'm defining the default role for the department. If I don't assign a role, this is what is going to be used.

Speaker 2

Mm-hmm.

Speaker 1

Effectively, I'm doing the same of what you're saying.

Speaker 2

Right. Okay.

Speaker 1

I tell you the complication of defining an explicit default role. You define an explicit default role, okay? Uh-

Speaker 2

Mm-hmm.

Speaker 1

For the department. Now, when they need to define a new role, I need to get that data of accessible fields from the default role.

Speaker 2

Okay.

Speaker 1

So instead of that, I'm putting it here because it-- what it is saying is that this is the scope of the data access for the departments.

Speaker 2

Mm-hmm.

Speaker 1

Benefit that you will get in your approach is that you don't need a master data of departments, mas-master table of departments. You can continue to do it the way you're doing right now. But, uh, I mean, you're, you're twisting a feature for your use. Lookup was not meant for these activities, right? Lookup was meant, yeah, in your explanation product and all that project and all that you need a lookup list, and you have it for that purpose.

Speaker 2

Correct.

Speaker 1

Tomorrow you provide a mechanism to delete a lookup list, then you have to add a additional business rule that you should not delete a department wala lookup list, otherwise it will create a big chaos.

Speaker 2

Right. Yeah. It will give you an extra, extra step for managing departments.

Speaker 1

Yes.

Speaker 2

And, uh, all this said, when we create a user, then we shouldn't make it mandatory to associate a user to any department.

Speaker 1

Why?

Speaker 2

Once you tag it to a department, it feels stagnant. He always has the option to add a user to any department that he would want. Once he does that, uh, all the department level default access, he will have all the department level default access. Right? But there is also a user, uh, who should not have, uh, even further finer, uh, granular level restriction based on data roles. So where he will be displayed, assign information page with the profile fields, address and telephone number and then a map, right? Within a-

Speaker 1

No, but if you, if you look at the physical world, a person always belongs to a department, right?

Speaker 2

Right.

Speaker 1

So why do you want to have a user who doesn't belong to a department?

Speaker 2

Mm-hmm.

Speaker 1

Because whatever rules you have for the department, they'll apply to him.

Speaker 2

Right.

Speaker 1

Okay. I, I can come up with an example that leadership theoretically doesn't belong to a single department. They oversee all the departments. So you can have a department for leadership and give them access to everything.

Speaker 2

They do that already. I think they have-

Speaker 1

Yeah. We are, we are already doing that, right? Yeah.

Speaker 2

Mm-hmm. But un-until we decide what access this department can have, then that can act as a default access, right?

Speaker 1

Yeah. So that's a matter of defining that when I say define a department, what checkboxes are by default selected and what are not. Right? That is what you're talking about.

Speaker 2

Right.

Speaker 1

Yeah. So, uh, that could be a kind of seed data or something, I don't know, or a hardcoded array.

Speaker 2

Mm-hmm.

Speaker 1

So right now, where are you getting the properties for any resource definition?

Speaker 2

Database.

Speaker 1

Huh?

Speaker 2

Database.

Speaker 1

Database specific column

Speaker 3

[coughs]

Speaker 1

Okay. But what Naveen is saying is that when I define a department, I don't want to check thirty fields, which is logical, okay? That I want to give access to these thirty fields. So the most common fields he would like to be prechecked.

Speaker 2

No, no, I'm not saying that.

Speaker 1

Then, okay, then I understood you wrong.

Speaker 2

So assuming that, uh, uh, a user belongs to a department, but Peter hasn't decided, uh, uh, as to what, uh, he-- what access he can have resource. So once we define the department, it's mandatory to select all these accessible columns, right? But he may want to discuss with leadership or with stakeholders as to what fields he can access from these data rows. So until that decision happens, a user will not belong to any department even though he has access to FTS roles. That is when he will just have access to site information page where he can see just the address of the site and then the telephone number and then nothing more.

Speaker 1

Yeah. So simple solution for that is that we define a department called default department. When a new user is created, till it is sorted out what access he wants to be given, unless it's already well known that he is belonging to RFT, so RFT department. If that is not known, he is assigned to default department and accordingly he has restrictions applied to the default department.

Speaker 2

Right.

Speaker 1

So we don't have to do anything special there. Yeah, I know it happens in our company also that people join in and we have not decided what project we are going to put them on. So their access is limited to only a certain repository and certain projects in Redmine.

Speaker 2

Yeah. And with that also, so we have these permissions also, right? Rahul, can you go to that page, roles page? You can. I don't know. I'll just wait. So for example, definitely this is permissions tab, right? Assuming that the user may do not want to give access to this staff information page or whatever. We disable view permission or modify, modify, search permission. Correct? Here. So he doesn't have anything. He doesn't have any access to staff module. So when he doesn't have any access to staff module, should we still define the default access or accessible columns for that department?

Speaker 1

I'm sorry, can you repeat that? Slightly mentally distracted.

Speaker 2

Assuming that a department doesn't get to see anything in staff module.

Speaker 1

Okay.

Speaker 2

Okay. How do we handle? So we are defining that accessible list, right? The department list. But here in the roles page, I say that I don't give access to the staff module.

Speaker 1

Only that.

Speaker 2

Only that.

Speaker 1

Okay. So I might-- now thinking, no thinking either, so I might be completely off the mark. In the department definition, while we are storing the list of accessible fields, we can also have a flag which says whether he has access to this particular resource.

Speaker 3

Sir. In manage department, there is a flag. For FTS user, all the activities should be there. But here we are making changes for IC admission. So we are giving permission, suppose. We don't want to show staff page to IC admission. So we have removed the view permission. So we have removed the column which has staff field. That's it.

Speaker 1

Is there any permission which is implied here or here?

Speaker 2

No.

Speaker 1

Staff list is there, but we can't see. Is everything by explicitly?

Speaker 3

No, sir.

Speaker 1

If I remove the view permission, will my name go away?

Speaker 2

Yes.

Speaker 1

No?

Speaker 3

No, staff information will be there.

Speaker 1

And if I make a call to API, it will give me an authorized list. Find whether 200 will go or unauthorized will go. Then Naveen, we can block from here, no? The user doesn't have role management permission, and he doesn't have view permission for the staff, so then he can't see.

Speaker 2

Then he can't see, but why will he get shown that in the department page? That list in the department page.

Speaker 3

Naveen, suppose we remove staff view permission for IC admission role, then we will hide the staff field from here. We won't show it.

Speaker 1

Wait a second. You are saying in the role that this user should not be able to see, but that department should not be able to see. And that is right, that rollout center should not be able to see anything about staff. If I go and do it in every role, even at the department level, I should not be able to see.

Speaker 3

If you want to do it at the department level, you can do it there.

Speaker 1

And if I do it at the department level, then I will not get this block because this department's role does not have access to staff.

Speaker 3

No, I think role-wise, it is not there.

Speaker 1

You want to block it for all the users of that department, right?

Speaker 2

Correct.

Speaker 1

Yeah. So then it should be blocked at the department level rather than role level.

Speaker 3

So then we will get a flag whether it has permission or not.

Speaker 1

Whether staff is accessible, who checks that? We need to do that checking.

Speaker 3

And the departments that are listed now, department name. So where will we get it from?

Speaker 1

Department masters.

Speaker 3

No. Department next FTS, RFT.

Speaker 1

That will come from department masters. There will be a separate table for departments. Okay. In which the name of the department, the access that has been granted to it will be there, and it will do a flag, or it will be a part of that, whether staff has access or not.

Speaker 3

Meaning we can create a department in manage department.

Speaker 1

Correct.

Speaker 3

Okay. Suppose I create an FTS department. I create an FTS department, name the department FTS, give its description which is related to FTS. Will this staff etc. come after creating or while creating?

Speaker 1

It can come while creating.

Speaker 3

Okay. So for FTS member, we will know that this is going to come. So other VIC, STS.

Speaker 1

ऐसा array resource है। This full JSON will go and sit in that department. Okay? So ऐसे ही staff access है, उसकी accessible fields हैं। ये process इस पर भी काम करना। Okay? दो team को रखना, ठीक ही चल।

Speaker 3

ठीक है। बाकी लिए आओ।

Speaker 1

So इस array में हम इस SI accordingly इसके लिए भी तू ना for example, comma man, man says, she is a boss. Public banking की क्या religion है इसका? Now when you assign the department to a role depending on whatever was enabled, आप उतने ही accordingly चीज दिखाओगे। ठीक है। Man यदि मेरे को accessible नहीं है तो man की permission हमें कैसे पता चलेगी? ठीक है। मिला?

Speaker 3

हाँ ये तो मिला।

Speaker 1

चलो फिर।

Speaker 3

तो अभी FPS के लिए जैसे staff वगैरह हमें पता है कि FPS में staff का क्या रहेगा उसमें। अभी तू आएगा अगर permission है तो नहीं आएगा permission नहीं है तो। बाकी के लिए फिर detail से discuss करके। ठीक है।

Speaker 1

बहुत change आती है अभी case में। So proper estimate करके नवीन को बताओ so that he can complete it. Principal use तो आपने दिखा दिया है। UI wise dramatic change नहीं है। यहां पे क्या है default जाके accessible आ रहा है। Okay. Okay. Operating behavior में थोड़ा correct but उसको उसे correct नहीं करेगा। और इसका time estimate निकालो क्योंकि ये काफी सारा काम है और properly document करो क्या behavior आने वाला है so that even before we implement he can go through it. नवीन, what do you?

Speaker 2

Yeah, I don't see any of the major changes. Instead of it being driven by roles, we'll create a new department table and the page there. So, Karan and Rahul, what is the estimate?

Speaker 5

So, नवीन today is we'll start with the documentation first what we discussed till now. So, from today we'll be working on documentation only. So we'll verify it with clear the concept and from tomorrow I guess we'll start working on that.

Speaker 1

So department management तो आपका basically group setting होता है largely. Okay. हम object driven कर रहे हैं क्योंकि वो जैसा भी हमने JSON लिखा ना, उसका database level पर model नहीं है, वो JSON है objects है। Okay। तो वो तो मेरे ख्याल से बहुत तेजी से मिल जाएगा। उसको इसका UI बनाना है which is a drawn from this। यहां की क्या वही mark करना है। Okay। काफी help करता है इसमें। इसमें थोड़े changes हैं।

Speaker 3

तो ये department manage department और ये भी हो जाएगा। लेकिन इसके हिसाब से बाकी के page में reflection करने के लिए थोड़ा ज्यादा है।

Speaker 1

नहीं, अभी बताऊं क्या है। उसने proper API expose की ना तो आपको सिर्फ API बदलनी है कि मुझे list चाहिए है accessible fields की। वो API देगा। आप आज भी field दिखा रहे हो। मुझे नहीं मालूम hardcoded है, कहां से आती है। तो आपको वो API call करके list में क्यों नहीं दिखानी?

Speaker 3

Okay। नहीं मैं, क्योंकि अभी जो branch है ना, काफी सारा code ये मेरे से, तो मैंने branch में ही code करना start कर दिया।

Speaker 1

ठीक है। Anyway, पहले document करो, task list बनाओ कि इस page में ये change है, इस page में ये change है। वो एक काम आपका क्या, पूछ जाकर हर एक का भी time देखो कि ये करने में मुझे कितना time लगेगा। Total timing कर लो। Don't try to estimate like clearly लेकिन ऐसा मत करो। Task list बनाओ, हर एक का rate डालिए क्योंकि इस काम को करने में इतना time लगेगा। ठीक है। Clarity है?

Speaker 2

Yes.

Speaker 1

Go and do that.

Speaker 3

थोड़ा मैं कर रही थी dashboard भी हमने अभी क्या change किया है।



 
