"""Generate small bundled, pitched practice tones for the virtual keyboard."""
import math
import os
import struct
import wave

ROOT = os.path.join(os.path.dirname(__file__), "assets", "notes")
os.makedirs(ROOT, exist_ok=True)
NAMES = ["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"]
RATE = 22050
for semitone, name in enumerate(NAMES):
    frequency = 261.626 * 2 ** (semitone / 12)
    samples = bytearray()
    for frame in range(int(RATE * 0.65)):
        t = frame / RATE
        envelope = math.exp(-4.0 * t)
        tone = (math.sin(2 * math.pi * frequency * t)
                + 0.32 * math.sin(4 * math.pi * frequency * t)
                + 0.13 * math.sin(6 * math.pi * frequency * t))
        samples.extend(struct.pack("<h", int(max(-1, min(1, tone * envelope)) * 12000)))
    with wave.open(os.path.join(ROOT, f"{name}.wav"), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(RATE)
        output.writeframes(samples)
