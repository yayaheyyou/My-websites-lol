using System;

namespace Me_trying_to_learn_new_things
{
    class Program6
    {
        static void Main(string[] args)
        { 
          // Styling cause why not lol.
         Console.ForegroundColor = ConsoleColor.Blue;
          
          // Main 

          string[] students = new string[4];

          Console.WriteLine("Enter 4 names of students.");

          for (int i = 0; i < students.Length; i++)
          {
               students[i] = Console.ReadLine();
          }

          Console.WriteLine("\nHere they are alphabetically");

          Array.Sort(students);

          for (int i = 0; i < students.Length; i++)
          {
              Console.WriteLine(students[i]);
          }

          // Closing line.
            Console.ReadKey();
        }
    }
}
