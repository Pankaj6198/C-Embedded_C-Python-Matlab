%Remove any variables in memory space 
clear all; close all; 

% First we will be loading image

img =imread('pankaj.jpg');
figure('Name','Original Image'); imshow(img); 

% Now let's convert into grayscale image
gray_img=rgb2gray(img);
figure('Name','Gray Scale Image'); imshow(gray_img); 

%Get Fourier Transform of an image
F = fft2(gray_img);
figure('Name','Fourier transform of an image'); imshow(abs(F), []); 

%Get the centered spectrum
Fsh = fftshift(F);
figure('Name','Centered fourier transform of Image'); imshow(abs(Fsh), []); 

%apply log transform
log_img = log(1+abs(Fsh));
figure('Name','Log fourier transform of Image'); imshow(log_img, []);

%reconstruct the Image
F = ifftshift(Fsh);
f = ifft2(F);
figure('Name','Reconstructed Image'); imshow(f, []);
