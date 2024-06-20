function chaotic_image_encryption()
    % Load the image
    img = imread('F:\encryption\Arnold_cat_Map\animal_farm.png');
    
    % Check if the image is grayscale or color
    [rows, cols, channels] = size(img);
    if channels == 1
        img = repmat(img, [1, 1, 3]); % Convert grayscale to color for consistent processing
    end
    
    % Ensure the image is 512x512
    img = imresize(img, [512 512]);
    
    % Convert image to double for processing
    img = im2double(img);
    
    % Apply Arnold Cat Map
    iterations = 50; % Number of iterations for Arnold Cat Map
    encrypted_img_cat = arnold_cat_map(img, iterations);
    imwrite(encrypted_img_cat, 'encrypted_arnold_cat.png');
    
    % Decrypt Arnold Cat Map
    decrypted_img_cat = arnold_cat_map_decrypt(encrypted_img_cat, iterations);
    imwrite(decrypted_img_cat, 'decrypted_arnold_cat.png');
    
    % Apply Henon Map
    a = 1.4;
    b = 0.3;
    iterations = 50; % Number of iterations for Henon Map
    encrypted_img_henon = henon_map(img, a, b, iterations);
    imwrite(encrypted_img_henon, 'encrypted_henon.png');
    
    % Decrypt Henon Map
    decrypted_img_henon = henon_map_decrypt(encrypted_img_henon, a, b, iterations);
    imwrite(decrypted_img_henon, 'decrypted_henon.png');

end
