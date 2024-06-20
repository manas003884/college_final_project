function decrypted_img = henon_map_decrypt(img, a, b, iterations)
    [M, N, C] = size(img);
    decrypted_img = img;
    for c = 1:C
        channel = img(:,:,c);
        [X, Y] = meshgrid(1:N, 1:M);
        for k = 1:iterations
            newX = mod(floor((X - 1) / b), N) + 1;
            newY = mod(floor((Y - 1 - b*newX) / a), M) + 1;
            channel = interp2(channel, newX, newY, 'nearest');
        end
        decrypted_img(:,:,c) = channel;
    end
end