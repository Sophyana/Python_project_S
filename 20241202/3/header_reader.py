import struct


def read_wav_header(file_path):
    try:
        with open(file_path, 'rb') as f:
            header = f.read(44)

            if len(header) < 44:
                return "NO"

            riff, file_size, wave = struct.unpack('<4sI4s', header[:12])
            if riff != b'RIFF' or wave != b'WAVE':
                return "NO"

            audio_format, channels, sample_rate, byte_rate, block_align, bit_depth = struct.unpack(
                '<HHIIHH',
                header[20:36]
            )

            data_marker, data_size = struct.unpack('<4sI', header[36:44])
            if data_marker != b'data':
                return "NO"

            result = (
                f"Size={file_size}, Type={audio_format}, Channels={channels}, "
                f"Sample Rate={sample_rate}, Bit Depth={bit_depth}, Data Size={data_size}"
            )
            return result

    except Exception:
        return "I cannot read this file."



file_path = input()
print(read_wav_header(file_path))