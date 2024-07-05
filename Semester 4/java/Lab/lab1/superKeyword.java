class Person{
    Person()
    {
        System.out.println("Person class Constructor");
    }
}
class Student extends Person{
    Student()
    {
        super();
        System.out.println("Student class Constructor");
    }
}
class superKeyword{
    public static void main(String args[])
    {
        new Student();
    }
}