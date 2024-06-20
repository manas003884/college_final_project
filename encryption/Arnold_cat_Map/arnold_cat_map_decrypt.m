function decrypted_img = arnold_cat_map_decrypt(img, iterations)
    [N, ~, C] = size(img);
    decrypted_img = img;
    for c = 1:C
        channel = img(:,:,c);
        for k = 1:iterations
            new_channel = zeros(N);
            for x = 1:N
                for y = 1:N
                    newX = mod((2*x - y - 1), N) + 1;
                    newY = mod((-x + y + N), N) + 1;
                    new_channel(newX, newY) = channel(x, y);
                end
            end
            channel = new_channel;
        end
        decrypted_img(:,:,c) = channel;
    end
end