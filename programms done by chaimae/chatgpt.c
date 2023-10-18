#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

void insertAtPosition(Node** head, int value, int position) {
    if (position < 0) {
        printf("La position doit être un nombre positif ou nul.\n");
        return;
    }

    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = NULL;

    if (*head == NULL) {
        // La liste est vide, donc on crée un nouveau nœud et on le définit comme la tête de la liste
        *head = newNode;
        return;
    }

    if (position == 0) {
        // On insère le nouveau nœud en tant que nouvelle tête de la liste
        newNode->next = *head;
        (*head)->prev = newNode;
        *head = newNode;
        return;
    }

    Node* current = *head;
    int count = 0;
    while (current->next != NULL && count < position - 1) {
        current = current->next;
        count++;
    }

    if (count < position - 1) {
        // La position spécifiée dépasse la taille de la liste
        printf("La position spécifiée dépasse la taille de la liste.\n");
        free(newNode);
        return;
    }

    newNode->next = current->next;
    newNode->prev = current;
    if (current->next != NULL) {
        current->next->prev = newNode;
    }
    current->next = newNode;
}

void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    Node* head = NULL;

    insertAtPosition(&head, 1, 0);
    insertAtPosition(&head, 3, 1);
    insertAtPosition(&head, 5, 2);
    insertAtPosition(&head, 7, 1);

    printf("Liste : ");
    printList(head);

    return 0;
}