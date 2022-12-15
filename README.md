## Sprouts

### Greenhouse Management and Monitoring System


Big Plans are afoot.  Stay Tuned!


### Components


There are currently two components envisioned.  

Work is underway to capture greenhouse "telemetry" and send that somewhere in 
"the cloud" where existing tools can be leveraged.  This is partly new work, but the sensor array that uses an arduino system I developed is still capable transmitting data on its XBee gizmo.  Unfortunately, the 
microcomputer that used to receive that data, and store it in an RRD database where it could be viewed using some tool, now mostly forgotten, long ago died and most everything associated with it has been lost.
(sort of like if the Voyager spacecraft survived, but everyone on Earth and our systems perished.)

A new, Raspberry Pi system with an XBee module will be built to receive this data, and send it to the cloud.

Initially, I'm planning to send the data as metrics to Cloud Logging facility in GCP.  There may be better/cheaper alternatives out there, so cost will become a consideration.


The second application will be an "operations manager" that can organize plants, observations and activities having to do with them.
This is a system that has been on the drawing board, to replace/upgrade the google doc and spreadsheet I use now (albeit inconsistently).  It's early stages on this one, but a few ideas have come together.
I learned enough Python recently to be able to knock out a simple system.  Future courses will skill me at proper db operations.





