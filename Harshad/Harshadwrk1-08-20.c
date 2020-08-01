//Writen a menu driven program with the following options: 1. Addition 2. Odd-Even
void main()
{
  int choice,a,b,s;
  printf("1. Addition\n2. Odd-Even");
  printf("\n Enter your choice ");
  scanf("%d",&choice);
  switch (choice) {
    case 1:
          printf("Enter two numbers ");
          scanf("%d%d",&a,&b);
          s = a + b;
          printf("Sum is\n%d",s);
          break;
    case 2:
          printf("Enter a number ");
          scanf("%d",&a);
          if (a % 2 == 0)
          {
            printf("Even Number");
          }
          else
          {
            printf("Odd Number");
          }
          break;
  }
}
