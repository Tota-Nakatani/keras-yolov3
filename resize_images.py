import os
#コマンドライン引数でpyファイルを実行する際にはsysをインポート
import sys
from glob import glob

from PIL import Image


def resize_images(images_dir, image_save_dir, image_size):
    #os.mkdirとは違い中間ディレクトリーも作成できる
    #exist_ok=True:存在していてもエラーを吐かない
    os.makedirs(image_save_dir, exist_ok=True)

    img_paths = glob(os.path.join(images_dir, '*'))

    for img_path in img_paths:
        # resize
        image = Image.open(img_path)
        rgb_im = image.convert('RGB')
        #Resize:新しい画像として生成する。アスペクト比は変化する。
        #thumbnail:元の画像に変更を加える(破壊),アスペクト比は維持される。
        rgb_im.thumbnail([image_size,image_size])

        # make background
        back_ground = Image.new("RGB", (image_size,image_size), color=(255,255,255))
        back_ground.paste(rgb_im)

        # make path
        #os.path.bassename:ファイル名を取得して保存先にパスを通す。
        save_path = os.path.join(image_save_dir, os.path.basename(img_path))
        #.までの文字列を取得
        end_index = save_path.rfind('.')
        save_path = save_path[0:end_index]+'.jpg'
        print('save',save_path)
        back_ground.save(save_path,quality=95,format='JPEG')


def _main():
    images_dir = 'images/'  # input directory
    image_save_dir = 'resize_image/'  # output directory
    image_size = 320
    if len(sys.argv) > 1:
        image_size = int(sys.argv[1])

    resize_images(images_dir=images_dir, image_save_dir=image_save_dir, image_size=image_size)


if __name__ == '__main__':
    _main()
