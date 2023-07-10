class RegressionModel:
    """RegressionModel class represents a regression model."""

    def __init__(self, name):
        """Initialize the RegressionModel object with a name."""
        self.name = name

    def train(self, input_data):
        """
        Train the regression model using the input data.

        Args:
            input_data: The input data required for training the model.
        """
        # Placeholder for the actual training logic of the regression model
        print(f"{self.name} is trained with input data: {input_data}")

    def predict(self, input_data):
        """
        Predict the output using the trained regression model.

        Args:
            input_data: The input data required for making predictions.
        """
        # Placeholder for the actual prediction logic of the regression model
        print(f"{self.name} predicts output for input data: {input_data}")
        return f"Prediction by {self.name}"


class ModelPipeline:
    """ModelPipeline class represents the regression model pipeline."""

    def __init__(self):
        """Initialize the ModelPipeline object."""
        self.models = []

    def add_model(self, model):
        """
        Add a regression model to the pipeline.

        Args:
            model: The regression model to add.
        """
        self.models.append(model)

    def process_data(self, input_data):
        """
        Process the input data through the pipeline.

        Args:
            input_data: The input data to be processed.
        """
        for i, model in enumerate(self.models):
            if i == 0:
                model.train(input_data)
            else:
                input_data = model.predict(input_data)


# Example usage
pipeline = ModelPipeline()

# Create regression models
model1 = RegressionModel("Model 1")
model2 = RegressionModel("Model 2")
model3 = RegressionModel("Model 3")

# Add models to the pipeline
pipeline.add_model(model1)
pipeline.add_model(model2)
pipeline.add_model(model3)

# Process data through the pipeline
input_data = "Input Data"

pipeline.process_data(input_data)
