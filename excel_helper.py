import json
import openpyxl

def write_data_to_file(data, year):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f'BluRay-{year}'

    headers = [
        'Title', 'Title Sub Heading', 'Production Company', 'Production Year', 'Film Time', 'Rating', 'Disc Release Date', 'Video Codec', 'Video Encoding', 'Video Resolution', 'Video Aspect Ratio', 'Original Aspect Ratio', 'Audio', 'Subtitles', 'Discs', 'Packaging', 'Playback', 'Digital', 'Genres', 'ISBN', 'EAN', 'UPC', 'SKU(Amazon)', 'eBay EPID', 'New Price', 'Used Price', '3rd Party Used Current', '3rd Party Used Average', 'Amazon Price Current', 'Amazon Price Average', 'Description', 'Director', 'Writer', 'Starring', 'Producers', 'Blu-Ray.com URL', 'Internet Movie Database URL', 'Rotten Tomatoes URL', 'SALIENT ID', 'Front Photo', 'Back Photo', 'Screenshots'
    ]

    ws.append(headers)
    
    for movie in data:
        if movie:
            row = [
                movie.get('title', ''),
                movie.get('subheading_title', ''),
                movie.get('production', ''),
                movie.get('production_year', ''),
                movie.get('runtime', ''),
                movie.get('age_rating', ''),
                movie.get('release_date', ''),
                movie.get('codec', ''),
                movie.get('encoding', ''),
                movie.get('resolution', ''),
                movie.get('aspect_ratio', ''),
                movie.get('original_aspect_ratio', ''),
                movie.get('audio', ''),
                movie.get('subtitles', ''),
                ','.join(movie.get('discs', [])),
                ','.join(movie.get('packaging', [])),
                ','.join(movie.get('playback', [])),
                ','.join(movie.get('digital', [])),
                ','.join(movie.get('genres', [])),
                movie.get('isbn', ''),
                movie.get('ean', ''),
                movie.get('upc', ''),
                movie.get('sku', ''),
                movie.get('epid', ''),
                movie.get('new_price', ''),
                movie.get('used_price', ''),
                movie.get('third_used_current_price', ''),
                movie.get('third_used_average_price', ''),
                movie.get('amazon_current_price', ''),
                movie.get('amazon_average_price', ''),
                movie.get('description', ''),
                movie.get('directors', ''),
                movie.get('writers', ''),
                movie.get('starring', ''),
                movie.get('producer', ''),
                movie.get('blu_ray_url', ''),
                movie.get('imdb_url', ''),
                movie.get('rt_url', ''),
                movie.get('', ''),
                movie.get('front_s3_url', ''),
                movie.get('back_s3_url', ''),
                ','.join(movie.get('screenshot_s3_urls', [])),
            ]

            ws.append(row)

    file_name = f'excels/BluRay-{year}.xlsx'
    wb.save(file_name)
    print(f'Data successfully written to {file_name}')

if __name__ == '__main__':
    # with open('data/BluRay-1998.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    
    # write_data_to_file(data, 1998)
    pass