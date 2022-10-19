using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VirtualSim;

namespace VirtualSimDemo
{
    public class Program
    {
        static void Main(string[] args)
        {
            DataManager dm = new DataManager();

            // Establish connection
            int connectionStatus = dm.Connect();
            if (connectionStatus >= 1)
            {
                Console.WriteLine("Connection successful.");

                // Set destination settings.
                dm.SetSourceAndDestinationAddress(220, 0, 15, 15);

                if (dm.LoadXML(@"C:\Users\gannabm\Desktop\WriteTableSample\VirtualSim\bin\Debug\ControlMapping_30XV_Pitbull_IMPERIAL_V10.xml"))
                {
                    Console.WriteLine("Loading XML successful.");

                    // Start writing tables.
                    dm.StartWritingTables(new byte[] { 11, 4, 5, 7, 8 });
                }
                else
                {
                    Console.WriteLine("Loading XML failed.");
                }

            }
            else
                Console.WriteLine("Unable to establish connection");

            int oatValue = 1;
            while (true)
            {
                // Modify point value.
                dm.UpdatePointValue("OAT", oatValue++);
                Console.Read();
            }
        }
    }
}
