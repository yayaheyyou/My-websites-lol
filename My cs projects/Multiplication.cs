using System;

namespace Me_trying_to_learn_new_things
{
    class Program
    {
        static void Main(string[] args)
        { 
          // Styling cause why not lol.
         Console.ForegroundColor = ConsoleColor.Blue;


         // Declaring variables.
         double num01;
         double num02;


          // Main.
         // First input.
         Console.Write("Input a number: ");

         num01 = Convert.ToDouble(Console.ReadLine());
 
         // Second input.
         Console.Write("Input a second number: ");

         num02 = Convert.ToDouble(Console.ReadLine());

         // Result.
         double result = num01 * num02;
   
         Console.WriteLine("The result is " + result);

         // Ending
         Console.ReadLine();

         Console.WriteLine("Okay bye!");

         Console.WriteLine("Press any key to escape.");

          // Closing line.
            Console.ReadKey();
        }
    }
}
