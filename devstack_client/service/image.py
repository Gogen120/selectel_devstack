def list_images(conn):
    return conn.list_images()


def find_image(conn, image_name):
    return conn.compute.find_image(image_name)
