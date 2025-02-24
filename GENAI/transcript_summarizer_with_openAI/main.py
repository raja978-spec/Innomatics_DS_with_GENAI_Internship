from openai import OpenAI
import ffmpeg

key = open(r'GENAI\key\.openai.txt').read().strip()

openAPIModel = OpenAI(api_key=key)

# for i in openAPIModel.models.list():
#     print(i)

#          MODEL FOR AUDIO TO TEXT CONVERSION

'''
 There a model called whisper-1 takes audio as it's input and produce
 in open API, but it takes only 25MB audio file. If you want to pass
 large file then you have to cut it by 25 25 parts
'''

#  Reduce file size with ffmpeg (It is efficient for large data)
input_file = r'GENAI\transcript_summarizer_with_openAI\sample_audio\audio.mp3'
output_file = r'GENAI\transcript_summarizer_with_openAI\sample_audio\shrinked_audio.mp3'

start_time = "00:00:10"  # Start at 10 seconds
duration = "20"  # Keep 20 seconds

ffmpeg.input(input_file, ss=start_time, t=duration).output(output_file).run()
print('Output saved')

# def generate_transcript(audio_file):
#     transcript = openAPIModel.audio.transcriptions.create(
#         file=audio_file,
#         model='whisper-1',
#         response_format='text'
#         )
#     return transcript

# audio_file = open(r'GENAI\transcript_summarizer_with_openAI\sample_audio\audio.mp3', 'rb')

# transcript = generate_transcript(audio_file)

# print(transcript)
