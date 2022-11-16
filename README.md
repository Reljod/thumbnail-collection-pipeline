# thumbnail-collection-pipeline
A thumbnail image collection pipeline that collects raw thumbnail from different videos and converts into trainable, suitable collection of images with useful metadata.

## Pipeline model
Since this is just a mini pipeline for demostration purposes, this pipeline will be just a mono repo that holds all the parts of the pipeline together. In real world scenario, different parts of the pipeline are mono-repo itself or maybe compose of different microservices, depending on the software architecture.

For demonstration purpose, this will only compose of the following:
1. Collection side
2. Data processing side
3. Data storage
4. Consume

### Collection Side
This is where we do the collection of raw data from different sources. For demo purpose, this is just gonna be a simple Web form.

### Data processing side
This is where we process raw data into more meaningful data depending on the use case. For demo purposes, it will just do the following processes:
1. Extracts metadata and compile it with the image.
2. Data augmentation
	- For bigger pictures, divide pictures into multiple sub pictures.
	- Rotate or skew the picture.
	- Add background noises.
3. Crop image.

### Data storage
This is where we store all the image data that goes through the pipeline. From raw data that we collect, to processed data and metadata that we extract, we want all of this to be properly stored.

Consists of:
- Data storage for raw data and metadata
- Data storage for processed data and metadata

### Consume
This is where we expose the processed images for usage. For demo purposes, we will just build a graphql API that returns all the images metadata and image address based on the request/categories.

The consume side will consists of:
- GraphQL API
- Simple web app