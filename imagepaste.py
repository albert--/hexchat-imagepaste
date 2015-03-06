import hexchat
import tempfile
from os import remove
from PIL import ImageGrab
from imgurpython import ImgurClient

__module_name__ = "hexchat-imagepaste"
__module_author__ = "albert--"
__module_version__ = "1.0"
__module_description__ = "Paste images from your clipboard using imgur.com by pressing Alt +"

client_id = "YOUR CLIENT ID"
client_secret = "YOUR CLIENT SECRET"

def imagepaste(word, word_eol, userdata):
	if not (word == ['43', '8', '+', '1']):
		return
	
	try:
		tempf = tempfile.NamedTemporaryFile(delete=False)
		img = ImageGrab.grabclipboard()
		img.save(tempf, "PNG")
	except:
		return
	
	tempfn = tempf.name
	
	client = ImgurClient(client_id, client_secret)
	up = client.upload_from_path(tempfn)
	
	tempf.close()
	remove(tempfn)
	
	cmd = "say " + up['link']
	print("Deletelink: http://imgur.com/delete/" + up['deletehash'])
	
	hexchat.command(cmd)
	return hexchat.EAT_ALL

def unload_imagepaste(userdata):
	print(__module_name__, "version", __module_version__, "unloaded.")

hexchat.hook_print("Key Press", imagepaste)
hexchat.hook_unload(unload_imagepaste)
print(__module_name__, "version", __module_version__, "loaded.")
