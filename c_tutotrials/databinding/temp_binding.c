#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>


// Mode: Holds the tempearture data
typedef struct {
	float temperature;
} Model;

// View: Displays the temperature data
typedef void (*ViewUpdateFunc)(float);

void displayTemperature(float temperature){
	printf("Current Tempearture: %.2fC\n", temperature);
}

// controller: Updates the model and notifies the view
typedef struct {
	Model * model;
	ViewUpdateFunc viewUpdate;
} Controller;

void updateTemperature(Controller * controller, float newTemperature){
	// update the model
	controller->model->temperature = newTemperature;
	// Notify the view
	if(controller->viewUpdate){
		controller->viewUpdate(controller->model->temperature);
	}

}

// simulate reading tempeature from a sensor
float readTemperatureSensor(){
	// Generate a random temperature between -10.0C and 40.0C
	return ((float)rand() / (float)(RAND_MAX)) * 50.0f - 10.0f;
}


int main(){
	// initialize random see
	srand(time(0));

	// initialize the model
	Model model;
	model.temperature = 0.0f;

	// initialize the controller
	Controller controller;
	controller.model = &model;
	controller.viewUpdate = displayTemperature;

	// simulate temperature monitoring
	for(int i=0; i<10; i++){
		float newTemperature = readTemperatureSensor();
		updateTemperature(&controller, newTemperature);
		sleep(1); // delay for 1 second to simulate real-time monitoring
	}	

	return 0;
}
























