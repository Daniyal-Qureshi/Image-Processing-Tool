using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using Microsoft.VisualBasic;
namespace WindowsFormsApplication1
{


    public partial class Form1 : Form
    {
        String image;
        public Form1()
        {
           InitializeComponent();
            image = null;
        }

        //Open dialog Button
        private void openFile(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png";
            ofd.Title = "Select image";
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    picbox.Image = new Bitmap(ofd.FileName);
                    image = ofd.FileName;
                    Console.WriteLine(image);
                    picbox.SizeMode = PictureBoxSizeMode.StretchImage;
                }
                catch (Exception ex) {}
            }

        }


        //python connectivity
        public void pythonBackend(String args)
        {
            
            Process p = new Process();
            Console.WriteLine("started");
            p.StartInfo = new ProcessStartInfo()
            {
                FileName = @"C:\Users\Daniyal\AppData\Local\Programs\Python\Python37-32\python.exe",
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true,
                Arguments = args
            };
            p.Start();
            Console.WriteLine("process has exited " + p.HasExited);
            string output = "";
            
            while (!p.HasExited) {
                output += p.StandardOutput.ReadToEnd();
            
            }
            output += p.StandardOutput.ReadToEnd();
         
            Console.WriteLine("process has exited " + p.HasExited);

            Console.WriteLine("image name " + output);
          if (output.Length >= 1)
             picbox.Image = new Bitmap(output);
              
        }
    
        //filter method    

        private void filter(object sender, EventArgs e)
        {

            RadioButton btn = (RadioButton)sender;
            String args = "";
            if (btn.Text == "Laplacian")
                args = string.Format("{0} {1} {2}", @"filters.py", btn.Text, image);
       

            else
            {
                String kernel = Microsoft.VisualBasic.Interaction.InputBox("Single dimension required", "Kernel Size");
                if (kernel.All(char.IsDigit) && kernel.Length >= 1 && kernel.Length <= 2)
                    args = string.Format("{0} {1} {2} {3}", @"filters.py", btn.Text, kernel, image);
                else
                {

                    MessageBox.Show("Enter correct input", "Invalid input", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

            }

            pythonBackend(args);
        }
        //noise
        private void noise(object sender, EventArgs e)
        {
            RadioButton btn = (RadioButton)sender;
            String args = "";

            if (btn.Text.Equals("Salt") || btn.Text.Equals("Pepper"))
            {
                String response = Microsoft.VisualBasic.Interaction.InputBox("Enter random number range seperated by comma (min,max)", btn.Text + " noise range");
                String[] kernel = response.Split(',');
                try
                {
                    if (Int32.Parse(kernel[1]) > Int32.Parse(kernel[0]))
                    {
                        args = string.Format("{0} {1} {2} {3}", @"noise.py", btn.Text, response, image);
                        pythonBackend(args);
                    }

                    else
                        throw new Exception();
                }
                catch (Exception ax)
                {
                    MessageBox.Show("Enter correct range", "Invalid range", MessageBoxButtons.OK, MessageBoxIcon.Error);

                }

                

            }

            else if (btn.Text.Equals("Gaussian"))
            {
                String response = Microsoft.VisualBasic.Interaction.InputBox("mean and sigma values seperated by comma (mean,sigma)", "Gaussian noise Mean and Sigma");
                String[] kernel = response.Split(',');
                try
                {
                    float min = float.Parse(kernel[0]);

                    min = float.Parse(kernel[1]);
                    args = string.Format("{0} {1} {2} {3}", @"noise.py", btn.Text, response, image);
                    pythonBackend(args);

                }
                catch (Exception ax)
                {
                    MessageBox.Show("Enter correct range", "Invalid range", MessageBoxButtons.OK, MessageBoxIcon.Error);

                }

            }
            else{
                args = string.Format("{0} {1} {2}", @"noise.py", btn.Text, image);
                pythonBackend(args);
            
            }



        }

        //intensity   
        private void intensitybox(object sender, EventArgs e)
        {
            ComboBox btn = (ComboBox)sender;

            String range = Microsoft.VisualBasic.Interaction.InputBox("Enter tha range of intensities separated by comma", "Intensities Operation");
            String[] ranges = range.Split(',');
            try
            {
                if (!(Int32.Parse(ranges[0]) >= 0 && Int32.Parse(ranges[1]) <= 255))
                    throw new Exception();

                int intensity = Int32.Parse(Microsoft.VisualBasic.Interaction.InputBox("Enter the value on which you want to perform the operation", "Operation value"));
            
                String args = string.Format("{0} {1} {2} {3} {4}", @"basic.py", btn.Text, range, image,intensity);
                pythonBackend(args);

            }
            catch (Exception ax)
            {
                MessageBox.Show("Enter correct range", "Invalid range", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }



        }

        private void basic(object sender, EventArgs e)
        {
           
            RadioButton btn = (RadioButton)sender;
            if (btn.Text == "Original image")
                picbox.Image = new Bitmap(image);
            else  
           pythonBackend(string.Format("{0} {1} {2} ", @"basic.py", btn.Text.Replace(" ",""), image));

        }

       //edge detection

        private void edge(object sender, EventArgs e)
        {
            RadioButton btn = (RadioButton)sender;
            if (btn.Text.Equals("Canny"))
            {

                try
                {
                    String response = Microsoft.VisualBasic.Interaction.InputBox("Enter threshold seperated by comma (thres1,thres2)", "Canny Threshold");
                    String[] r = response.Split(',');
                    int thres = Int32.Parse(r[0]);
                    thres = Int32.Parse(r[1]);
                    pythonBackend(string.Format("{0} {1} {2} {3}", @"edges.py", btn.Text, response, image));

                }
                catch (Exception ax)
                {
                    MessageBox.Show("Enter correct threshold", "Invalid input", MessageBoxButtons.OK, MessageBoxIcon.Error);


                }


            }

            else {

                pythonBackend(string.Format("{0} {1} {2}", @"edges.py", btn.Text,image));           
            }



        }
        //button hist
        private void hist_click(object sender, EventArgs e)
        {
            this.Hide();
            histogram hmg = new histogram(image);
            hmg.ShowDialog();
         
            this.Close();
        }

        private void save(object sender, EventArgs e)
        {
            SaveFileDialog svd = new SaveFileDialog();
            svd.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png";
            svd.Title = "Save image";
            if (svd.ShowDialog() == DialogResult.OK) {
                Bitmap b = new Bitmap(picbox.Image);
                b.Save(svd.FileName);
         
            }


        }



       
    }
       
}
