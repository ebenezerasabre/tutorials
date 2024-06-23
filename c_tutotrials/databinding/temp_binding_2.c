#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>


#define SENSOR_COUNT 3
#define LOG_FILE "temperature_log.txt"


struct Model;
struct Controller;

// Model: Holds the temperature data and thresholds
typedef struct Model {
	float temperatures[SENSOR_COUNT];
	float upperThreshold;
	float lowerThreshold;
} Model;

// View: Displays the temperature data and logs it
typedef void (*ViewUpdateFunc)(float[], int);

void displayTemperatures(float temperatures[], int count){
	printf("Current temperatures: ");
	for(int i=0; i<count; i++){
		printf("%.2fC ", temperatures[i]);
	}
	printf("\n");
}

void logTemperatures(float temperatures[], int count){
	FILE * file = fopen(LOG_FILE, "a");
	if(file == NULL){
		printf("Error opening log file\n");
		return;
	}
	for(int i=0; i<count; i++){
		fprintf(file, "%.2f ", temperatures[i]);
	}
	fprintf(file, "\n");
	fclose(file);

}

// Controller: Updates the model and notifies the view
typedef struct Controller {
	Model * model;
	ViewUpdateFunc viewUpdate;
} Controller;

void checkThresholds(Controller * controller){
	for(int i=0; i<SENSOR_COUNT; i++){
		if(controller->model->temperatures[i] > controller->model->upperThreshold)
			printf("Alarm: Temperatures %.2f exceeds upper threshold\n", controller->model->temperatures[i]);
		if(controller->model->temperatures[i] < controller->model->lowerThreshold)
			printf("Alarm: Temperatures %.2f below lower threshold\n", controller->model->temperatures[i]);

	}

}

void updateTemperatures(Controller * controller, float newTemperatures[]){
	for(int i=0; i<SENSOR_COUNT; i++)
		controller->model->temperatures[i] = newTemperatures[i];

	// Notify the view
	if(controller->viewUpdate)
		controller->viewUpdate(controller->model->temperatures, SENSOR_COUNT);

	// log the temperatures
	logTemperatures(controller->model->temperatures, SENSOR_COUNT);

	// Check the thresholds
	checkThresholds(controller);

}

// Simulate reading tempeatures from sensors
void readTemperatureSensors(float temperatures[]){
	for(int i=0; i<SENSOR_COUNT; i++){
		temperatures[i] = ((float)rand() / (float)(RAND_MAX)) * 50.0f - 10.0f;
	}

}

//User Interface: set thresholds and control monitoring
void setThresholds(Model * model){
	printf("Enter upper threshold: ");
	scanf("%f", &model->upperThreshold);
	printf("Enter lower threshold: ");
	scanf("%f", &model->lowerThreshold);
}


int main(){
	 // Initialize random see
	 srand(time(0));

	 // Initialize the model
	 Model model;
	 for(int i=0; i < SENSOR_COUNT; i++)
		 model.temperatures[i] = 0.0f;

	 model.upperThreshold = 30.0f;
	 model.lowerThreshold = 0.0f;

	 // initiailize the controller
	 Controller controller;
	 controller.model = &model;
	 controller.viewUpdate = displayTemperatures;

	 // user sets thresholds
	 setThresholds(&model);

	 // Simulate temperature monitoring
	 for(int i=0; i<10; i++){
		float newTemperatures[SENSOR_COUNT];
		readTemperatureSensors(newTemperatures);
		updateTemperatures(&controller, newTemperatures);
		sleep(1); // Delay for 1 second to simulate real-time monitoring
	 }


	return 0;
}







