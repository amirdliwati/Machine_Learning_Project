using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.CV.CvEnum;
using System.IO;

namespace MultiFaceRec
{
    class Cl_FaceFeatures
    {

        //Declararation of all variables, vectors and haarcascades
        Image<Bgr, Byte> currentFrame;
        Capture grabber;
        HaarCascade Haar_face;
        HaarCascade Haar_mouth;
        HaarCascade Haar_eye;
        MCvFont font = new MCvFont(FONT.CV_FONT_HERSHEY_TRIPLEX, 0.5d, 0.5d);
        Image<Gray, byte> Face_Cropped, Eye_Cropped, Mouth_Cropped, TrainedFace = null;
        Image<Gray, byte> gray = null;

        public List<double> From_Picture(Image<Bgr, Byte> img, out List<Point> _list_points)
        {
            List<double> _list_dimentions = new List<double>();
            _list_points = new List<Point>();

            //Load haarcascades for face detection
            Haar_face = new HaarCascade("haarcascade_frontalface_default.xml");
            Haar_mouth = new HaarCascade("mouth.xml");
            //Haar_mouth = new HaarCascade("haarcascade_mcs_mouth.xml");
            Haar_eye = new HaarCascade("eye.xml");


            //
            Image<Gray, Byte> Face_Cropped_Bottom = null;
            Image<Gray, Byte> Face_Cropped_Top = null;

            Image<Gray, Byte> Eye_Cropped_L = null;
            Image<Gray, Byte> Eye_Cropped_R = null;

            MCvAvgComp f_eyeL = new MCvAvgComp();
            MCvAvgComp f_eyeR = new MCvAvgComp();
            MCvAvgComp f_mouth = new MCvAvgComp();

            //Convert it to Grayscale
            gray = img.Convert<Gray, Byte>();

            //Face Detector
            MCvAvgComp[][] facesDetected = gray.DetectHaarCascade(
                Haar_face, 1.2, 10,
                HAAR_DETECTION_TYPE.DO_CANNY_PRUNING,
                new Size(20, 20));


            //Action for each element detected
            if (facesDetected[0].Length != 0)
            {
                MCvAvgComp f = facesDetected[0][0];

                Face_Cropped = img.Copy(f.rect).Convert<Gray, byte>().Resize(200, 200, INTER.CV_INTER_CUBIC);
                //draw the face detected in the 0th (gray) channel with blue color
                img.Draw(f.rect, new Bgr(Color.Red), 2);

                var rect_Bottom = new Rectangle(0, (3 * Face_Cropped.Rows) / 4, Face_Cropped.Cols, Face_Cropped.Rows / 4);
                Face_Cropped_Bottom = Face_Cropped.Copy(rect_Bottom).Convert<Gray, byte>();

                var rect_Top = new Rectangle(0, 0, Face_Cropped.Cols, Face_Cropped.Rows / 2);
                Face_Cropped_Top = Face_Cropped.Copy(rect_Top).Convert<Gray, byte>();

                #region Eyes Detection

                // Find Eyes
                MCvAvgComp[][] eyes_detected = Face_Cropped.DetectHaarCascade(
                    Haar_eye, 1.1, 1,
                    HAAR_DETECTION_TYPE.DO_CANNY_PRUNING,
                    new Size(40, 40));
                if (eyes_detected[0].Length != 0)
                {
                    f_eyeR = eyes_detected[0][0];
                    Eye_Cropped_R = Face_Cropped.Copy(f_eyeR.rect).Convert<Gray, byte>();

                    if (eyes_detected[0].Length == 2)
                    {
                        f_eyeL = eyes_detected[0][1];
                        Eye_Cropped_L = Face_Cropped.Copy(f_eyeL.rect)
                            .Convert<Gray, byte>();//.Resize(100, 100, INTER.CV_INTER_CUBIC);
                    }
                }

                #endregion

                #region Mouth Setection

                MCvAvgComp[][] Mouth_detected = Face_Cropped_Bottom.DetectHaarCascade(
                    Haar_mouth, 1.1, 1,
                    HAAR_DETECTION_TYPE.DO_CANNY_PRUNING,
                    new Size(30, 30));
                if (Mouth_detected[0].Length != 0)
                {
                    f_mouth = Mouth_detected[0][0];
                    Mouth_Cropped = Face_Cropped_Bottom.Copy(f_mouth.rect)
                        .Convert<Gray, byte>();//.Resize(100, 100, INTER.CV_INTER_CUBIC);
                }

                #endregion

                #region Show Results

                _list_points = results(Face_Cropped,
                    Mouth_Cropped, f_mouth,
                    Eye_Cropped_L, Eye_Cropped_R,
                    f_eyeL, f_eyeR);
                /*
                for (int i = 0; i < _list_points.Count; i++)
                {
                    Face_Cropped.Draw(new CircleF(
                        new Point(_list_points[i].X, _list_points[i].Y), 1),
                        new Gray(1.0), 3);
                }
                */
                #endregion

                #region Show Dimentions
                
                if (_list_points.Count == 6)
                {
                    //txt_Dimentions.Text += "Left Eye Width=" +
                    _list_dimentions.Add(Distance(_list_points[0], _list_points[1]));
                    //txt_Dimentions.Text += "Right Eye Width=" +
                    _list_dimentions.Add(Distance(_list_points[2], _list_points[3]));
                    //txt_Dimentions.Text += "Mouth Width=" +
                    _list_dimentions.Add(Distance(_list_points[4], _list_points[5]));
                    //txt_Dimentions.Text += "Distance 1 Between Eyes=" +
                    _list_dimentions.Add(Distance(_list_points[0], _list_points[3]));
                    //txt_Dimentions.Text += "Distance 2 Between Eyes=" +
                    _list_dimentions.Add(Distance(_list_points[1], _list_points[2]));
                    //txt_Dimentions.Text += "Distance 1 Between Left Eye and Mouth Left Corner=" +
                    _list_dimentions.Add(Distance(_list_points[0], _list_points[4]));
                    //txt_Dimentions.Text += "Distance 2 Between Left Eye and Mouth Left Corner=" +
                    _list_dimentions.Add(Distance(_list_points[1], _list_points[4]));
                    //txt_Dimentions.Text += "Distance 1 Between Left Eye and Mouth Left Corner=" +
                    _list_dimentions.Add(Distance(_list_points[3], _list_points[5]));
                    //txt_Dimentions.Text += "Distance 2 Between Left Eye and Mouth Left Corner=" +
                    _list_dimentions.Add(Distance(_list_points[2], _list_points[5]));
                }
                else
                {
                    //txt_Dimentions.Text = "Not enough Information";
                }

                #endregion
            }
            return _list_dimentions;
        }

        private void harris(Image<Gray, Byte> _im_input
            , out Image<Gray, Byte> im_ThresholdImage
            , out Image<Gray, float> im_Corners)
        {
            Image<Gray, Byte> _im_output = new Image<Gray, byte>(_im_input.Size);

            // Corners Detection
            im_Corners = new Image<Gray, float>(_im_input.Size);
            CvInvoke.cvCornerHarris(_im_input, im_Corners, 3, 3, 0.01);

            // create and show inverted threshold image
            im_ThresholdImage = new Image<Gray, Byte>(_im_input.Size);
            CvInvoke.cvThreshold(im_Corners, im_ThresholdImage, 0.0001, 255.0, Emgu.CV.CvEnum.THRESH.CV_THRESH_BINARY_INV);

            //_im_output = m_ThresholdImage;
            //_im_output = im_Corners.Convert<Gray, byte>();
        }

        private Image<Gray, Byte> CannyEdge(Image<Gray, Byte> img_in)
        {
            Image<Gray, Byte> imgSmooth = img_in.SmoothGaussian(3);

            Gray cannyThreshold = new Gray(149);
            Gray cannyThresholdLinking = new Gray(149);

            //Image<Gray, Byte> bin = gray.ThresholdBinary(new Gray(149), new Gray(255));
            Image<Gray, Byte> cannyEdges = img_in.Canny(cannyThreshold, cannyThresholdLinking);

            return cannyEdges;

        }

        private List<Point> results(Image<Gray, Byte> face_cropped,
            Image<Gray, Byte> Mouth_Cropped, MCvAvgComp f_mouth,
            Image<Gray, byte> Eye_Cropped_L, Image<Gray, byte> Eye_Cropped_R,
            MCvAvgComp f_eyeL, MCvAvgComp f_eyeR)
        {
            List<Point> _list_points = new List<Point>();
            Image<Gray, byte> Eye_Cropped_Canny_L;
            Image<Gray, byte> Eye_Cropped_Canny_R;
            Image<Gray, byte> Mouth_Cropped_Canny;


            int x, y;

            try
            {
                Eye_Cropped_Canny_L = CannyEdge(Eye_Cropped_L);

                #region Left Eye
                // Eye Left outside Corner
                for (int j = 0; j < Eye_Cropped_Canny_L.Cols; j++)
                {
                    for (int i = Eye_Cropped_Canny_L.Rows - 1; i > Eye_Cropped_Canny_L.Rows / 3; i--)
                    {
                        if (Eye_Cropped_Canny_L[i, j].Intensity == 255)
                        {
                            x = f_eyeL.rect.X + j;
                            y = f_eyeL.rect.Y + i;
                            
                            _list_points.Add(new Point(x, y));

                            //
                            j = Eye_Cropped_Canny_L.Cols;
                            i = Eye_Cropped_Canny_L.Rows;
                            break;

                        }

                    }
                }

                // Eye Left inside Corner
                for (int j = Eye_Cropped_Canny_L.Cols - 1; j > 0; j--)
                {
                    for (int i = Eye_Cropped_Canny_L.Rows - 1; i > Eye_Cropped_Canny_L.Rows / 3; i--)
                    {
                        if (Eye_Cropped_Canny_L[i, j].Intensity == 255)
                        {
                            x = f_eyeL.rect.X + j;
                            y = f_eyeL.rect.Y + i;
                            
                            _list_points.Add(new Point(x, y));

                            //
                            j = 0;
                            i = Eye_Cropped_Canny_L.Rows;
                            break;
                        }
                    }
                }
                #endregion
            }
            catch
            {
                //MessageBox.Show("error:left eye");
            }
            try
            {
                Eye_Cropped_Canny_R = CannyEdge(Eye_Cropped_R);

                #region Right Eye
                // Eye Right inside Corner
                for (int j = 0; j < Eye_Cropped_Canny_R.Cols; j++)
                {
                    for (int i = Eye_Cropped_Canny_R.Rows - 1; i > Eye_Cropped_Canny_R.Rows / 3; i--)
                    {
                        if (Eye_Cropped_Canny_R[i, j].Intensity == 255)
                        {
                            x = f_eyeR.rect.X + j;
                            y = f_eyeR.rect.Y + i;
                            
                            _list_points.Add(new Point(x, y));

                            //
                            j = Eye_Cropped_Canny_R.Cols;
                            i = Eye_Cropped_Canny_R.Rows;
                            break;

                        }

                    }
                }

                // Eye Right outside Corner
                for (int j = Eye_Cropped_Canny_R.Cols - 1; j > 0; j--)
                {
                    for (int i = Eye_Cropped_Canny_R.Rows - 1; i > Eye_Cropped_Canny_R.Rows / 3; i--)
                    {
                        if (Eye_Cropped_Canny_R[i, j].Intensity == 255)
                        {
                            x = f_eyeR.rect.X + j;
                            y = f_eyeR.rect.Y + i;
                            
                            _list_points.Add(new Point(x, y));

                            //
                            j = 0;
                            i = Eye_Cropped_Canny_R.Rows;
                            break;
                        }
                    }
                }
                #endregion
            }
            catch
            {
                //MessageBox.Show("error:Right Eye");
            }

            try
            {
                Mouth_Cropped_Canny = CannyEdge(Mouth_Cropped);

                #region Mouth
                // Mouth Left Corner
                for (int j = 0; j < Mouth_Cropped_Canny.Cols; j++)
                {
                    for (int i = 0; i < Mouth_Cropped_Canny.Rows; i++)
                    {
                        if (Mouth_Cropped_Canny[i, j].Intensity == 255)
                        {
                            x = f_mouth.rect.X + j;
                            y = f_mouth.rect.Y + i + (3 * face_cropped.Rows) / 4;
                            _list_points.Add(new Point(x, y));

                            //
                            j = Mouth_Cropped_Canny.Cols;
                            i = Mouth_Cropped_Canny.Rows;
                            break;

                        }

                    }
                }

                // Mouth Right Corner
                for (int j = Mouth_Cropped_Canny.Cols - 1; j > 0; j--)
                {
                    for (int i = 0; i < Mouth_Cropped_Canny.Rows; i++)
                    {
                        if (Mouth_Cropped_Canny[i, j].Intensity == 255)
                        {
                            x = f_mouth.rect.X + j;
                            y = f_mouth.rect.Y + i + (3 * face_cropped.Rows) / 4;
                            _list_points.Add(new Point(x, y));

                            //
                            j = 0;
                            i = Mouth_Cropped_Canny.Rows;
                            break;
                        }
                    }
                }
                #endregion
            }
            catch
            {
                //MessageBox.Show("error:Mouth");
            }

            return _list_points;
        }

        private double Distance(Point P1, Point P2)
        {
            return Math.Round(
                Math.Sqrt(
                    Math.Pow((P1.X - P2.X), 2)
                    + Math.Pow((P1.Y - P2.Y), 2)
                    )
                    , 2);
        }


    }
}
