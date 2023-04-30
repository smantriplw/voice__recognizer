taken from https://audio-samples.github.io/

convert mp3 to wav:
for f in *.mp3; do ffmpeg -i "$f" -acodec pcm_s16le -ac 1 -ar 16000 "${f%.mp3}.wav"; done