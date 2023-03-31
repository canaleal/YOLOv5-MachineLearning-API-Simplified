

<div align="center">

  <h1>Machine Learning API</h1>
  <h4>GIS  •  Machine Learning  •  Data Processing</h4>

</div>


<h1>Contents</h1>

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Development](#development)
- [Calling API](#calling)
- [FAQ](#faq)

<h1 id="introduction">Introduction</h1>

The machine learning API is a simplified version of the Ultralytics Yolov5 Machine Learning project. This tool is meant to serve as a reusable project for data processing and simple configuration. You can even add your own models by dragging them into the weights folder and changing just 1 variable in the process_video.py file. 



<h1 id="technologies">Technologies</h1>

<div align="center" id="technologies">

Below is a table that provides an overview of the technologies we are currently working with for this project.

<table>
  <tr> 
    <td align='center'><img src="https://img.shields.io/badge/numpy-%2320232a.svg?style=for-the-badge&logo=numpy" alt="NumPy"/></td>
    <td align='center'><img src="https://img.shields.io/badge/pandas-%2320232a.svg?style=for-the-badge&logo=pandas" alt="Pandas"/></td>
    <td align='center'><img src="https://img.shields.io/badge/pytorch-%2320232a.svg?style=for-the-badge&logo=pytorch" alt="PyTorch"/></td>
    <td align='center'><img src="https://img.shields.io/badge/scikit_learn-%2320232a.svg?style=for-the-badge&logo=scikit-learn" alt="scikit-learn"/></td>
  </tr>
  <tr>
    <td align='center'><img src="https://img.shields.io/badge/matplotlib-%2320232a.svg?style=for-the-badge&logo=matplotlib" alt="Matplotlib"/></td>
    <td align='center'><img src="https://img.shields.io/badge/tensorflow-%2320232a.svg?style=for-the-badge&logo=tensorflow" alt="TensorFlow"/></td>
    <td align='center'><img src="https://img.shields.io/badge/keras-%2320232a.svg?style=for-the-badge&logo=keras" alt="Keras"/></td>
    <td align='center'><img src="https://img.shields.io/badge/scipy-%2320232a.svg?style=for-the-badge&logo=scipy" alt="SciPy"/></td>
  </tr>
 </table>
</div>

<h1 id="development">Development</h1>


### Setup
Create a virtual enviroment using python 3.10 and activate it.
```bash
python3.10 -m venv myenv
```

Activate the virtual environment by running the activate script. On macOS and Linux, run:
```
source myenv/bin/activate
```
On Windows, run:
```
myenv\Scripts\activate.bat
```

After activating the virtual environment, you should see the name of your environment in your terminal prompt.

### Install

Use the package manager [PIP](https://pypi.org/project/pip/) to install the dependencies.

```bash
pip install -r requirements.txt
```

To start the application, use [Fast API](https://fastapi.tiangolo.com/tutorial/first-steps/).

```bash
uvicorn main:app --reload
```

<h1 id="calling">Calling API</h1>

The API expects a json key value pair:
```json
{
    "video_link": "Whatever your link is"
}
```

The API returns a StreamingResponse in mp4 format. Streaming responses return the video in smaller chunks/ packets instead of one large response. 
You can fetch the processed video and turn it into a usable video source link with the following JAVASCRIPT function:
```javascript
async function getVideo(my_video_link) {
	try {

		let data = JSON.stringify({
			video_link: my_video_link
		});

		let config = {
			method: 'post',
			url: 'http://127.0.0.1:8000/dashcam/machinelearning',
			headers: {
				'Content-Type': 'application/json'
			},
			body: data
		};

		let response = await fetch(config.url, config);
		let videoBlob = await response.blob();
		processed_video_link = URL.createObjectURL(videoBlob);
	} catch (error) {
		console.log(error);
	}
}
```

<h1 id="faq">FAQ</h1>

## Do I need a GPU?
No, the model works for both CPUs and GPUs. However, using a GPU can significantly speed up the processing time. CPUs are around 5x to 10x slower than GPUs for video processing.

On a Nvidia 3080 GPU, the model takes 6 ms per frame or 0.9 seconds to process a 5-second video.

On a AMD Ryzen 7 5800X CPU, the model takes 30 ms per frame or 4.5 seconds to process a 5-second video.

## How do I use a GPU?
To use your GPU, you must have PyTorch and CUDA installed on your computer. Your GPU must have CUDA cores, which are usually available in Nvidia graphics cards above the 2000 series.

Here is a tutorial to help you set up PyTorch and CUDA on Windows 10: [PyTorch & CUDA Setup - Windows 10](https://www.youtube.com/watch?v=GMSjDTU8Zlc)


