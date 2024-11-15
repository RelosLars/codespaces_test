# ML Training Project with Docker and GitHub Codespaces

This project demonstrates how to containerize a machine learning training pipeline using Docker. Below are the instructions to execute the project in various scenarios, including from the command line, with a Dockerfile, and within a GitHub Codespace.

Prerequisites
- Python 3.9 installed locally (if running from the command line).
- Docker installed (if using Docker locally).
- Git installed (if fetching this repo using git).

# Downloading the Project
You can download the following project using the command:

```bash
   git clone https://github.com/Ceredavide/MLOPS.git
```

# Running the Project

## 1. From the Command Line

If you want to run the project locally without Docker:
### 1.1	Install dependencies:
Fetch the necessary dependencies for this project using the following command:
```bash
   pip install -r requirements.txt
```


### 1.2 Start the Training Script

You can run the training script with optional hyperparameters. If no parameters are specified, the following default values will be used:

- `LEARNING_RATE`: `4e-05`
- `BATCH_SIZE`: `32`
- `WEIGHT_DECAY`: `0.1`
- `WARMUP_STEPS`: `50`
- `DROPOUT_RATE`: `0.6`

Example of running the script with the default values:
```bash
python src/train.py
```

You can override the defaults by passing the desired values as arguments:

```bash
python src/train.py --learning_rate 1e-04 --batch_size 64 --weight_decay 0.05 --warmup_steps 100 --dropout_rate 0.3
```
## 2. Using a Dockerfile

If you prefer to containerize the project:

###	2.1	Build the Docker image:

```bash
   docker build -t training_image .
```


###	2.2	Run the Docker container with default hyperparameters:

```bash
   docker run training_image
```

###	2.3	Optionally, override hyperparameters using environment variables:
The configurable hyperparameters are the same mentioned in the section 1.2
```bash
   docker run -e LEARNING_RATE=3e-05 -e BATCH_SIZE=64 training_image
```

## 3. Using GitHub Codespaces

To run the project in a GitHub Codespace, you can choose between two configurations:

### A. Existing Dockerfile
1. Ensure the Dockerfile is in the root or parent directory of the repository.
2. Open the repository in a Codespace.
3. This configuration automatically builds and runs the container using the devcontainer.json settings. Hyperparameters can be adjusted in the containerEnv section.
4. Training starts automatically upon container launch.

### B. Docker in Docker
1. Select the “Docker in Docker” configuration in the devcontainer.json file.
2. Open the repository in a Codespace.
3. The postCreateCommand builds the Docker image (my_training_image), creates the TensorBoard logs directory, and installs TensorBoard.
4. Run the training manually inside the Codespace by executing:

```bash
   docker run -e LEARNING_RATE=4e-05 -e BATCH_SIZE=32 my_training_image
```

## Monitoring with TensorBoard

To monitor training logs:
	1.	Open TensorBoard by forwarding port 6006 in your terminal or Codespace.
	2.	Navigate to http://localhost:6006 in your browser.

Notes
1. GPU support is required for efficient training. Performance may degrade significantly without GPU access, especially in Docker environments without GPU passthrough.
2. GitHub Codespaces is better suited for development and testing rather than heavy ML training in containers. Consider using Conda with Python notebooks for lighter workflows.
