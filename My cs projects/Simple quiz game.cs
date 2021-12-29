using System;

namespace Me_trying_to_learn_new_things
{
    class Program4
    {
        static void Main(string[] args)
        { 
          // Styling cause why not lol.
         Console.ForegroundColor = ConsoleColor.Blue;

         // Main


         // Declaring variables

         double Answer;
         double Answer2;

         // First condition.

         Console.WriteLine("What's (3 + 3 * 0) equal to?");

         Answer = Convert.ToDouble(Console.ReadLine());

         if ( Answer == 3 )
         {
            Console.WriteLine("Correct! :-)");
         }
         else {
             Console.WriteLine("Incorrect. :-(");
         }
          
         // Second condition.

         Console.WriteLine("Solve the following math problem:- if 1 = 3, 2 = 3, 3 = 5, 4 = 4 and 5 = 4 then 6 = ?");
          
          Answer2 = Convert.ToDouble(Console.ReadLine());

         if ( Answer2 == 3 )
         {
             Console.WriteLine("Correct! :-)");
         }
         else {
             Console.WriteLine("Incorrect. :-(");
         }
         Console.WriteLine("Press any key to escape.");
          // Closing line.
            Console.ReadKey();
        }
    }
}