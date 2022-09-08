# Bone Fracture Detection

This is an implementation of segmentation U-Net in Keras and Tensorflow to detect bone fractures in hand x-ray images. The model uses streamlit to create a better interface to interact with the model and predictions. 

![Sample of Interface on Streamlit](/assets/sample_of_Interface.png)

The weights of a pre-trained model of U-Net from Keras were adapted for this project. A collection of 236 images were used for training purposes and 39 images were used for validation purposes. Furthermore, Jaccard Loss function (also known as Intersection-over-union loss) was used as the loss function for this model. 

You will need to have `streamlit` downloaded on your local device to spin up the streamlit environment.

To run the streamlit application, follow these instructions: 
```
$clone the repo
$cd <repo>
$Broken Bone Detection Using X-Ray Images % streamlit run app.py 
```
