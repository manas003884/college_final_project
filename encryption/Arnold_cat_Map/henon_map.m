function encrypted_img = henon_map(img, a, b, iterations)
    [M, N, C] = size(img);
    encrypted_img = img;
    for c = 1:C
        channel = img(:,:,c);
        [X, Y] = meshgrid(1:N, 1:M);
        for k = 1:iterations
            newX = mod(floor(a*(X - Y.^2 + 1) + 1), N) + 1;
            newY = mod(floor(b*X + 1), M) + 1;
            channel = interp2(channel, newX, newY, 'nearest');
        end
        encrypted_img(:,:,c) = channel;
    end
end