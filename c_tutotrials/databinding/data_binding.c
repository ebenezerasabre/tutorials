#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Model: Holds the data
typedef struct {
	char data[100];
} Model;

// View: Displays the data
typedef void (*ViewUpdateFunc)(const char*);

void displayData(const char * data){
	printf("View: Data updated to: %s\n", data);

}

// controller: updates the model and notifies the view
typedef struct {
	Model * model;
	ViewUpdateFunc viewUpdate;

} Controller;

void updateModel(Controller * controller, const char * newData){
	// update the model
	strcpy(controller->model->data, newData);

	// notify the view
	if(controller->viewUpdate){
		controller->viewUpdate(controller->model->data);
	}


}

int main(){
	// Initialize the model
	Model model;
	strcpy(model.data, "Initail data");

	// Initialize the controller
	Controller controller;
	controller.model = &model;
	controller.viewUpdate = displayData;


	// display initial data
	displayData(controller.model->data);

	// update the model through the controller
	updateModel(&controller, "Hello, world");

	// update the model through the controller again
	updateModel(&controller, "Data Binding in C");


	return 0;
}



