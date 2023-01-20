
import logging
import subprocess
import os
import urllib.request
import shutil


def checkIfFolderExistsAndCreateIfNot(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def deleteFileIfItExists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def deleteAllFilesInFolder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logging.error(e)


def deleteAllFoldersInFolder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


# * Paths for project
input_folder_path = 'app/videos/input'
input_video_path = f'{input_folder_path}/video.mp4'

# * Paths for output
output_folder_path = 'app/videos/output'
output_video_path = f'{output_folder_path}/video.mp4v'
output_video_codec_path = f'{output_folder_path}/video-codec.mp4'
output_video_codec_compressed_path = f'{output_folder_path}/video-codec-comp.mp4'

# * Paths for YOLOV5
detect_python_path = 'app/detect.py'
weights = "app/weights/yolov5s.pt"


def callSubProcess(command):
    subprocess.call(command, shell=True)


def downloadVideoGivenURLAndSaveToPath(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        return path
    except Exception as e:
        logging.error(e)
        return e


def get_video_for_processing(video_link=''):
    try:

        # * Check if folders exist, if not create them
        checkIfFolderExistsAndCreateIfNot(input_folder_path)
        checkIfFolderExistsAndCreateIfNot(output_folder_path)

        # * Download the video
        downloadVideoGivenURLAndSaveToPath(video_link, input_video_path)

        # * Create the subprocess
        stride = 1
        process = f'python {detect_python_path} --weights {weights} --source {input_video_path} --vid-stride {stride} --conf-thres {0.4}'
        callSubProcess(process)

        # * Create ffmpeg process
        callSubProcess(f'ffmpeg -y -i {output_video_path} -map 0 -c copy {output_video_codec_path}')
        callSubProcess(f'ffmpeg -y -i {output_video_codec_path} -vcodec  libx264  {output_video_codec_compressed_path}')

        # * Delete all files (input, output)
        deleteAllFilesInFolder(input_folder_path)
        # deleteAllFilesInFolder(output_folder_path)

        # * Return the path to the new file
        return output_video_codec_compressed_path

    except Exception as e:
        logging.error(e)
        return e
