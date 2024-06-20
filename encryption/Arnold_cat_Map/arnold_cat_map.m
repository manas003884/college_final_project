function encrypted_img = arnold_cat_map(img, iterations)
    [N, ~, C] = size(img);
    encrypted_img = img;
    for c = 1:C
        channel = img(:,:,c);
        for k = 1:iterations
            new_channel = zeros(N);
            for x = 1:N
                for y = 1:N
                    newX = mod((x + y - 1), N) + 1;
                    newY = mod((x + 2*y - 2), N) + 1;
                    new_channel(newX, newY) = channel(x, y);
                end
            end
            channel = new_channel;
        end
        encrypted_img(:,:,c) = channel;
    end
end