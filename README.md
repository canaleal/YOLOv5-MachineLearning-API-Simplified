[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


# Machine Learning API
The machine learning API is a simplified version of the Ultralytics Yolov5 Machine Learning project. This tool is meant to serve as a reusable project for data processing and simple configuration. You can even add your own models by dragging them into the weights folder and changing just 1 variable in the process_video.py file. 

## Author
Alex Canales 

## Installation
Use the package manager [PIP](https://pypi.org/project/pip/) to install the dependencies.

```bash
pip install
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Starting the Application
To start the application, use [Fast API](https://fastapi.tiangolo.com/tutorial/first-steps/).

```bash
uvicorn main:app --reload
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## What does the API expect and return
The API expects a json key value pair:
```json
{
    "video_link": "Whatever your link is"
}
```
You can see more about what the API expects as input in the routes folder.

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Do I need a GPU?
The model works for both CPU and GPUs. 
Note, CPUs are around 5x to 10x slower than GPUs for processing videos. 

On a Nvidia 3080 it takes 6 ms per frame or 0.9second to process a 5 second video. 

On a 5800x it takes 30ms per frame or 4.5 second to process a 5 second video. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How do I use a GPU?
To use your GPU, you must have PyTorch & CUDA installed on your computer. As such, your GPU must have cuda cores (Usually anything above 2000 series Nvidia cards)

Use this tutorial if you need help:
[PyTorch & CUDA Setup - Windows 10](https://www.youtube.com/watch?v=GMSjDTU8Zlc)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Add your own model
Add your weights file to the weights folder. Don't for get to change the weights variable in the process_video.py to path of your new weights file. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/canaleal/YOLOv5-MachineLearning-API-Simplified.svg?style=for-the-badge
[contributors-url]: https://github.com/canaleal/YOLOv5-MachineLearning-API-Simplified/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/canaleal/YOLOv5-MachineLearning-API-Simplified.svg?style=for-the-badge
[forks-url]: https://github.com/canaleal/YOLOv5-MachineLearning-API-Simplified/network/members
[stars-shield]: https://img.shields.io/github/stars/canaleal/YOLOv5-MachineLearning-API-Simplified.svg?style=for-the-badge
[stars-url]: https://github.com/canaleal/YOLOv5-MachineLearning-API-Simplified/stargazers
[issues-shield]: https://img.shields.io/github/issues/canaleal/YOLOv5-MachineLearning-API-Simplified.svg?style=for-the-badge
[issues-url]: https://github.com/canaleal/YOLOv5-MachineLearning-API-Simplified/issues
[license-shield]: https://img.shields.io/github/license/canaleal/YOLOv5-MachineLearning-API-Simplified.svg?style=for-the-badge
[license-url]: https://raw.githubusercontent.com/canaleal/YOLOv5-MachineLearning-API-Simplified/main/LICENSE
