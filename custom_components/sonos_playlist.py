url = "http://192.168.0.140:5005/kitchen/playlists"
response = urllib.urlopen(url)
data = json.loads(response.read())

f = open("/home/hass/.homeassistant/extraconfig/input_select/sonos_playlists.yaml","w")

f.write("sonos_playlist:" + "\n")
f.write("  name: Playlist" + "\n")
f.write("  options:" + "\n")
for key in data:
  f.write("   - '" + key + "'\n")

f.write("  icon: 'mdi:playlist-check'" + "\n")
f.close()


## Shell commands
f = open("/home/hass/.homeassistant/extraconfig/shell_command/sonos_playlist.yaml","w")


for key in data:
  keyname = ''.join(e for e in key if e.isalnum()).lower()
  keyvalue = urllib.quote(key)
  f.write("sonos_playlist_" + keyname + ": '/usr/bin/curl +X http://192.168.0.140:5005/kitchen/playlist/" + keyvalue + "'\n")

f.close()
