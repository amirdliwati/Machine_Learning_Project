using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Emgu.CV;
using Emgu.Util;
using Emgu.CV.Structure;
using Emgu.CV.CvEnum;
using System.IO;
using System.Drawing;
using System.Net;


public partial class _Default : System.Web.UI.Page
{

    FaceFeatures face_features = new FaceFeatures();
    Image<Bgr, Byte> img1;
    List<double> _list_dimentions = new List<double>();
    protected void Page_Load(object sender, EventArgs e)
    {
        Image_url_clear();
        face_features.Haar_face_path = Server.MapPath("~/Haarcascade/haarcascade_frontalface_default.xml");
        face_features.Haar_mouth_path = Server.MapPath("~/Haarcascade/mouth.xml");
        face_features.Haar_eye_path = Server.MapPath("~/Haarcascade/eye.xml");
        face_features.Server_path_image_test = Server.MapPath("~/ImagesProcessing");


    }

    protected void BTN_Processing_Click(object sender, EventArgs e)
    {

        try
        {
            Delete_Dir();
            Save_Pic();
            img1 = new Image<Bgr, Byte>(Server.MapPath("~/ImagesProcessing/00.jpg"));
            _list_dimentions = face_features.From_Picture(img1);
            Images_url();
            Dimentions(_list_dimentions);
        }
        catch { }

    }

    protected void Dimentions(List<double> list_dimentions)
    {
        txt_Dimentions.Text = "";
        txt_Dimentions.Text += "Left Eye Width=" + list_dimentions[0].ToString() + "\r\n";
        txt_Dimentions.Text += "Right Eye Width=" + list_dimentions[1].ToString() + "\r\n";
        txt_Dimentions.Text += "Mouth Width=" + list_dimentions[2].ToString() + "\r\n";
        txt_Dimentions.Text += "Distance Small Between Eyes=" + list_dimentions[3].ToString() + "\r\n";
        txt_Dimentions.Text += "Distance Larg Eyes=" + list_dimentions[4].ToString() + "\r\n";
        txt_Dimentions.Text += "Distance Small Between Left Eye and Mouth Left Corner=" + list_dimentions[5].ToString() + "\r\n";
        txt_Dimentions.Text += "Distance Larg Between Left Eye and Mouth Left Corner=" + list_dimentions[6].ToString() + "\r\n";
        txt_Dimentions.Text += "Distance Small Between Right Eye and Mouth Right Corner=" + list_dimentions[7].ToString() + "\r\n";
        txt_Dimentions.Text += "Distance Larg Between Right Eye and Mouth Right Corner=" + list_dimentions[8].ToString() + "\r\n";    
    }

    protected void Image_url_clear()
    {
        imageBoxFrameGrabber.ImageUrl = "";
        Image2.ImageUrl = "";
        Image3.ImageUrl = "";
        Image1.ImageUrl = "";
        Image4.ImageUrl = "";
        Image5.ImageUrl = "";
        Image7.ImageUrl = "";
        Image8.ImageUrl = "";
        Image9.ImageUrl = "";
        Image10.ImageUrl = "";
        Image11.ImageUrl = "";
        Image12.ImageUrl = "";
        Image13.ImageUrl = "";
    }

    protected void Images_url()
    {

        imageBoxFrameGrabber.ImageUrl= "~/ImagesProcessing/00.jpg";
        Image2.ImageUrl = "~/ImagesProcessing/0.jpg";
        Image3.ImageUrl = "~/ImagesProcessing/2.jpg";
        Image1.ImageUrl = "~/ImagesProcessing/1.jpg";
        Image4.ImageUrl = "~/ImagesProcessing/4.jpg";
        Image5.ImageUrl = "~/ImagesProcessing/3.jpg";
        Image7.ImageUrl = "~/ImagesProcessing/R5.jpg";
        Image8.ImageUrl = "~/ImagesProcessing/R9.jpg";
        Image9.ImageUrl = "~/ImagesProcessing/L6.jpg";
        Image10.ImageUrl = "~/ImagesProcessing/L8.jpg";
        Image11.ImageUrl = "~/ImagesProcessing/7.jpg";
        Image12.ImageUrl = "~/ImagesProcessing/10.jpg";
        Image13.ImageUrl = "~/ImagesProcessing/11.jpg";

    }

    protected void Delete_Dir()
    {
        DirectoryInfo di = new DirectoryInfo(Server.MapPath("~/ImagesProcessing"));
        foreach (FileInfo file in di.GetFiles())
        {
            file.Delete();
        }
    }


    protected void Save_Pic()
    {
        try
        {
            string SavePath = AppDomain.CurrentDomain.BaseDirectory + "\\ImagesProcessing\\";
            if (FileUpload1.HasFile)
            {
                //SavePath += Server.HtmlEncode(FileUpload1.FileName);
                SavePath += Server.HtmlEncode("00.jpg");
                FileUpload1.SaveAs(SavePath);
            }
        }
        catch { }
    }


    protected void Button1_Click(object sender, EventArgs e)
    {
        Images_url();
    }
}