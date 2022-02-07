using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class box : Form
    {



        private static DialogResult ShowDialog()
        {

            Console.WriteLine("called");
            return new DialogResult();
        }
        
        
        public box(String title,String message)
        {
        }

        public box() {
            InitializeComponent();
        
        }

        private void button3_Click(object sender, EventArgs e)
        {
          

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            this.Close();
        }

        public string inti(String title,String message) {

            new box();
            return "s";
        }


    }
}
