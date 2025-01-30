void dequeue()
{
    if (this->isEmpty())
    {
        return;
    }

    Person *temp = this->front;
    this->front = this->front->next;

    if (this->front == NULL)
    {
        this->rear = NULL;
    }

    delete temp;
}