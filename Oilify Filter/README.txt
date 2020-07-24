oilify.py takes 4 parameters (img, N, R, γ);
where img is the name of the file as a string;
N for the local N-bin intensity histogram around the pixel at (xi, yi);
R is the window size of R x R around the pixel;
γ controls the amount of influence the strong value has on the output; 
the image in the folder was ran with the following command oilify("original.png", 10, 10, 10)