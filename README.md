## Sprouts

### Greenhouse Management and Monitoring System


Big Plans are afoot.  Stay Tuned!


### Components


There are currently two components envisioned.  

Work is underway to capture greenhouse "telemetry" and send that somewhere in 
"the cloud" where existing tools can be leveraged.  This is partly new work, but the sensor array that uses an arduino system I developed is still capable transmitting data on its XBee gizmo.  Unfortunately, the 
microcomputer that originally received that data, storing it into an RRD database (whisper, perhaps) where it could be viewed using some tool (Grafana, or a predecessor, I don't recall) long ago died and most everything associated with it has been lost.
(sort of like if the Voyager spacecraft survived, but everyone on Earth and our systems perished.)

A new, Raspberry Pi system with an XBee link will be built to receive this data, and send it to the cloud.

Initially, I'm planning to send the data as metrics to Cloud Logging facility in GCP.  There may be better/cheaper alternatives out there, so cost will be a consideration.


The second application will be an "operations manager" that can organize plants, observations and activities having to do with them.
This is a system that has been on the drawing board for quite a while, to replace/upgrade the google doc and spreadsheet I use now (albeit inconsistently).  It's early stages on this one, but a few ideas have come together.
I learned enough Python recently to be able to knock out a simple system.  Future courses will skill me at proper db and other operations.

## Motivation
This is mostly for fun and learning.  If you've stumbled upon this, you are welcome to watch, steal, criticize, or even contribute.  But that's not my intention.  

I'm taking a Python programming certificate and it's an easy and fun language to work with.  It also works well with inexpensive microcontrollers, which I envision will always be at the heart of any system like this.

I'm just pushing stuff to GitHub so it doesn't disappear the next time my hard drive crashes (which is what happened before).
You may also see various "starts" at similar projects elsewhere in my repo.  Well, I've been working with software for a long time, and that has come with many, many technology changes.
It's fun to think about a completely new system.  It's a lot of work to build any non-trivial thing.  Sometimes the benefits are worth the effort, or the benefits of the effort are enough to move the project forward.  Sometimes, they are not.  

I also don't want to fall into the telescope maker's trap (never going outside look at the stars because they're always building or tweaking their instruments.  Been there, done that already, before I was much of a gardener).  I garden year round, care for my growing soil (some of my beds are now more than 20 years, and healthier than ever!) My gardening plan is be able to eat food I grew any day of the year.  That will always take precedence over writing software (at least for myself).







