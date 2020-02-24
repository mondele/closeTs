#closeTs

A python script to write to the manifest of a .tstudio project folder to close chunks for existing chunk files. This is to speed the work of a technician supporting an event, or working remotely on a harvested event, where there is not the ability to verify the contents of the chunks independently.

Version 0.1 works on a single project folder. It looks for the `manifest.json` file to verify that the folder is a project, then recurses through the structure to see what chunks are present as text files in the files structure, and then adds them to the manifest.

**Planned Features**

The ability to add translator information to the manifest. Possibly some reporting tech.