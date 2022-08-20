import wave

obj = wave.open("mensaje.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("Parameters", obj.getparams())


# Time of the audio files in seconds

t_audio = obj.getnframes()/obj.getframerate()
print("Time in seconds: ", t_audio)
