import turicreate as tc
import numpy as np
import os

class BitmapData:
    random_state = np.random.RandomState(100)
    # Change if applicable
    quickdraw_dir = 'quickdraw'
    bitmaps_dir = os.path.join(quickdraw_dir, 'bitmaps')
    sframes_dir = os.path.join(quickdraw_dir, 'sframes')
    sframes_bitmap_dir = os.path.join(sframes_dir, 'bitmap_square_triangle.sframe')
    npy_ext = '.npy'
    num_examples_per_class = 100
    classes = ["square", "triangle"]
    num_classes = len(classes)

    def build_bitmap_sframe(self):
        bitmaps_list, labels_list = [], []
        for class_name in self.classes:
            class_data = np.load(os.path.join(self.bitmaps_dir, class_name + self.npy_ext))
            self.random_state.shuffle(class_data)
            class_data_selected = class_data[:self.num_examples_per_class]
            class_data_selected = class_data_selected.reshape(
                class_data_selected.shape[0], 28, 28, 1)
            for np_pixel_data in class_data_selected:
                FORMAT_RAW = 2
                bitmap = tc.Image(_image_data = np_pixel_data.tobytes(),
                                _width = np_pixel_data.shape[1],
                                _height = np_pixel_data.shape[0],
                                _channels = np_pixel_data.shape[2],
                                _format_enum = FORMAT_RAW,
                                _image_data_size = np_pixel_data.size)
                bitmaps_list.append(bitmap)
                labels_list.append(class_name)

        sf = tc.SFrame({"drawing": bitmaps_list, "label": labels_list})
        sf.save(os.path.join(self.sframes_dir, "bitmap_square_triangle.sframe"))
        return sf 
    
    def create_model(self):
        model = tc.drawing_classifier.create(input_dataset=self.sframes_bitmap_dir)
    
