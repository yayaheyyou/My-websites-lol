using System;

namespace Me_trying_to_learn_new_things
{
    class Program3
    {
        static void Main(string[] args)
        { 
          // Styling cause why not lol.
         Console.ForegroundColor = ConsoleColor.Blue;


         // Declaring variables.
         double num01;
         double num02;
         double num03;

          // Main. 


        // First input.

          Console.Write("Input a number: ");
          
         num01 = Convert.ToDouble (Console.ReadLine());

        // Second input.

           Console.Write("Input a second number: ");

           num02 = Convert.ToDouble(Console.ReadLine());

        // Third input.
       
            Console.Write("Input a third number:");

            num03 = Convert.ToDouble(Console.ReadLine());

        // Calculating the average.
         
         double result = (num01 + num02 + num03) /3;

        // The result.

           Console.WriteLine("The average is " + result);

          // Closing line.

            Console.ReadKey();
        }
    }
}