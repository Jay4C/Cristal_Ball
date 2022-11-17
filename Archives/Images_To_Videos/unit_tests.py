import unittest
import os
import cv2
from PIL import Image


class UnitTestsImagesToVideosArchieBlue(unittest.TestCase):
    # ok
    def test_video_1(self):
        print("test_video_1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Archie_Blue\\1"

        video_name = 'video_1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_2(self):
        print("test_video_2")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Archie_Blue\\2"

        video_name = 'video_2.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_3(self):
        print("test_video_3")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Archie_Blue\\3"

        video_name = 'video_3.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_4(self):
        print("test_video_4")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Archie_Blue\\4"

        video_name = 'video_a_b_4.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()


class UnitTestsImagesToVideosHydrogenContainer(unittest.TestCase):
    # ok
    def test_video_1(self):
        print("test_video_1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Hydrogen_Container"

        video_name = 'video_1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()


class UnitTestsImagesToVideosStanleyMeyer(unittest.TestCase):
    # ok
    def test_video_h_g_b(self):
        print("test_video_h_g_b")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Stanley_Meyer\\H_G_B"

        video_name = 'video_h_g_b.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_w_e_1(self):
        print("test_video_w_e_1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Stanley_Meyer\\W_E_1"

        video_name = 'video_w_e_1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_w_e_2(self):
        print("test_video_w_e_2")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Stanley_Meyer\\W_E_2"

        video_name = 'video_w_e_2.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_w_e_3(self):
        print("test_video_w_e_3")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Stanley_Meyer\\W_E_3"

        video_name = 'video_w_e_3.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_w_e_4(self):
        print("test_video_w_e_4")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos\\1_Holomorphe" \
                        "\\Stanley_Meyer\\W_E_4"

        video_name = 'video_w_e_4.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        # Finding the mean height and width of all images.
        # This is required because the video frame needs
        # to be set with same width and height. Otherwise
        # images not equal to that width height will not get
        # embedded into the video
        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()


class UnitTestsImagesToVideosSpecials(unittest.TestCase):
    # ok
    def test_video_us4324640A(self):
        print("test_video_us4324640A")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US4324640A"

        video_name = 'video_us4324640A.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_us3423942(self):
        print("test_video_us3423942")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US3423942"

        video_name = 'video_us3423942.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_US1061206A(self):
        print("test_video_US1061206A")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US1061206A"

        video_name = 'video_US1061206A.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_US20150188400A1(self):
        print("test_video_US20150188400A1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US20150188400A1"

        video_name = 'video_US20150188400A1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_US20020125774A1(self):
        print("test_video_US20020125774A1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US20020125774A1"

        video_name = 'video_US20020125774A1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_US3071705A(self):
        print("test_video_US3071705A")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US3071705A"

        video_name = 'video_US3071705A.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                im = Image.open(os.path.join(folder_images, file))

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_US6362718B1(self):
        print("test_video_US6362718B1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\US6362718B1"

        video_name = 'video_US6362718B1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                im = Image.open(os.path.join(folder_images, file))

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_edwin_gray(self):
        print("test_video_edwin_gray")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\Edwin_Gray"

        video_name = 'video_edwin_gray.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                im = Image.open(os.path.join(folder_images, file))

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_chas_campbell(self):
        print("test_video_chas_campbell")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\2_Specials\\Chas_Campbell"

        video_name = 'video_chas_campbell.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                im = Image.open(os.path.join(folder_images, file))

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_transmutator(self):
        print("test_video_transmutator")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\Transmutator"

        video_name = 'video_transmutator.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                im = Image.open(os.path.join(folder_images, file))

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_vmeg(self):
        print("test_video_vmeg")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG"

        video_name = 'video_vmeg.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                im = Image.open(os.path.join(folder_images, file))

                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()


class UnitTestsImagesToVideosMyInventions(unittest.TestCase):
    # ok
    def test_video_vmeg_flower_1(self):
        print("test_video_vmeg_flower_1")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG\\Flower\\1"

        video_name = 'video_vmeg_flower_1.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_vmeg_flower_2(self):
        print("test_video_vmeg_flower_2")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG\\Flower\\2"

        video_name = 'video_vmeg_flower_2.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_vmeg_flower_3(self):
        print("test_video_vmeg_flower_3")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG\\Flower\\3"

        video_name = 'video_vmeg_flower_3.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_vmeg_flower_4(self):
        print("test_video_vmeg_flower_4")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG\\Flower\\4"

        video_name = 'video_vmeg_flower_4.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_vmeg_flower_5(self):
        print("test_video_vmeg_flower_5")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG\\Flower\\5"

        video_name = 'video_vmeg_flower_5.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()

    # ok
    def test_video_vmeg_flower_6(self):
        print("test_video_vmeg_flower_6")

        folder_images = "A:\\1_Professionnel\\1_Holomorphe\\2_Archives\\2_Outils_Numeriques" \
                        "\\My_Tools\\Test\\Service\\Archives\\Images_To_Videos" \
                        "\\3_My_Inventions\\VMEG\\Flower\\6"

        video_name = 'video_vmeg_flower_6.avi'

        if os.path.exists(os.path.join(folder_images, video_name)):
            os.remove(os.path.join(folder_images, video_name))

        mean_height = 0
        mean_width = 0

        num_of_images = len(os.listdir(folder_images))

        for file in os.listdir(folder_images):
            im = Image.open(os.path.join(folder_images, file))
            width, height = im.size
            mean_width += width
            mean_height += height
            im.close()

        mean_width = int(mean_width / num_of_images)
        mean_height = int(mean_height / num_of_images)

        # Resizing of the images to give
        # them same width and height
        for file in os.listdir(folder_images):
            if file.endswith(".png"):
                # opening image using PIL Image
                im = Image.open(os.path.join(folder_images, file))

                # resizing
                imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
                imResize.save(os.path.join(folder_images, file), 'PNG', quality=95)  # setting quality
                im.close()

        # Video Generating function
        def generate_video():
            os.chdir(folder_images)

            images = [img for img in os.listdir(folder_images)
                      if img.endswith(".jpg") or
                      img.endswith(".jpeg") or
                      img.endswith(".png")]

            frame = cv2.imread(os.path.join(folder_images, images[0]))

            # setting the frame width, height width
            # the width, height of first image
            height, width, layers = frame.shape

            video = cv2.VideoWriter(video_name, 0, 1, (width, height))

            # Appending the images to the video one by one
            for image in images:
                video.write(cv2.imread(os.path.join(folder_images, image)))

            # Deallocating memories taken for window creation
            cv2.destroyAllWindows()
            video.release()  # releasing the video generated

        # Calling the generate_video function
        generate_video()


if __name__ == '__main__':
    unittest.main()
