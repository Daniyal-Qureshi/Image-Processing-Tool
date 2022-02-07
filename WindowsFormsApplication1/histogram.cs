using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class histogram : Form
    {
        String image;
        public histogram(String im)
        {
            InitializeComponent();
            image = im;
            this.pictureBox1.Image = new Bitmap(image);
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
        }


        public void pythonBackend(String args)
        {

            Process p = new Process();
            Console.WriteLine("started");
            p.StartInfo = new ProcessStartInfo()
            {
                FileName = @"C:\Users\Daniyal\AppData\Local\Programs\Python\Python36\python.exe",
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true,
                Arguments = args
            };
            p.Start();

            p.WaitForExit();
            string output = "";
            output = p.StandardOutput.ReadToEnd().Replace("\n", "");

            Console.WriteLine("process has exited " + p.HasExited);

            Console.WriteLine("image name " + output);
            if (output.Length >= 1)
                pictureBox1.Image = new Bitmap(output);

        }


        private void draw_hist(object sender, EventArgs e)
        {
            pythonBackend(string.Format("{0} {1} {2}", @"histogram.py", "Histogram", image));

        }   

        private void hist_equalization(object sender, EventArgs e)
        {
            String response = Microsoft.VisualBasic.Interaction.InputBox("Enter the number of iterations","Histogram Equalization iterations");
            try
            {
                pythonBackend(string.Format("{0} {1} {2} {3}", @"histogram.py", "HistogramEuqlization", image, Int32.Parse(response)));
            }
            catch (Exception ex) {
                MessageBox.Show("Enter correct iteration", "Invalid iteration",MessageBoxButtons.OK,MessageBoxIcon.Error);
            }
        }

        private void histogram_matching(object sender, EventArgs e)
        {
            String refe="";

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "Image files (*.jpg, *.jpeg, *.jpe, *.jfif, *.png) | *.jpg; *.jpeg; *.jpe; *.jfif; *.png";
            ofd.Title="Select reference image";
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                try
                {
                        refe=ofd.FileName;
                        pythonBackend(string.Format("{0} {1} {2} {3}", @"histogram.py", "HistogramMatching", image, refe));
                }
                catch (Exception ex) { }
            }
            

    
            
        }

        private void clos(object sender, FormClosedEventArgs e)
        {
            this.Hide();
            Form1 obj = new Form1();
            obj.ShowDialog();
            this.Close();

        }



    }



}
    