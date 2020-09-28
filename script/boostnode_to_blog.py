# -*- coding: utf-8 -*-

"""
Boostnode 转为 md 文档，然后发布到 hexo blog
"""
import json
import os

local_path = '/Users/beer/cloud/boostnote/beef/'
hexo_path = '/Users/beer/code/gravel/source/_posts/'
git_path = '/Users/beer/code/gravel'


def get_folder():
    with open(local_path + 'boostnote.json', 'r') as f:
        folders = json.load(f)
        folder_title_map = {}
        for item in folders.get('folders'):
            folder_title_map[item.get('key')] = item.get('name')
        return folder_title_map


def convert(title_map):
    node_path = local_path + 'notes'
    list_files = os.listdir(node_path)
    for file in list_files:
        path = node_path + '/' + file
        with open(path, 'r') as f:
            lines = f.readlines()
            date = lines[0].split(': "')[1].strip().split('T')
            created_at = date[0] + ' ' + date[1][0:8].strip('"')
            folder = lines[3].split(':')[1].strip()
            folder_title = title_map.get(folder.strip('"')).strip("'")
            title = lines[4].split(':')[1].strip().strip('"')
            tags = get_tags(lines)
            content = get_content(lines, tags)
            tags.append(folder_title)
            export_file(created_at, title, tags, content)


def get_content(lines, tags):
    if len(tags) == 0:
        return lines[8 + len(tags):-4]
    else:
        return lines[8 + len(tags) + 1:-4]


def get_tags(lines):
    tag_end = 0
    for i in range(5, len(lines)):
        if lines[i].strip() == ']' or lines[i].strip() == 'tags: []':
            tag_end = i
            break
    if tag_end == 5:
        return []
    tags = lines[6:tag_end]
    return [tag.strip() for tag in tags]


def export_file(created_at, title, tags, content):
    path = hexo_path + '/' + title.strip() + '.md'
    tags = [tag.strip().replace("'", "").replace('"', '') for tag in tags]
    with open(path, 'w') as f:
        lines = ['---\n',
                 'title: {}\n'.format(title),
                 'tags: [{}]\n'.format(','.join(tags)),
                 'date: {}\n'.format(created_at),
                 '---\n']

        final_content = []
        for line in content:
            line = line.strip()
            if line == line == '''''''':
                line = '\n'
            else:
                line = line + '\n'
            final_content.append(line)
        lines.extend(final_content)
        f.writelines(lines)


if __name__ == '__main__':
    os.system('rm -rf {} && mkdir {}'.format(hexo_path, hexo_path))

    title_map = get_folder()
    convert(title_map)

    # mv to hexo post target path
    os.system('cd {} && hexo clean && hexo g'.format(git_path))
    os.system('scp -r {} beer:/home/ubuntu/beef'.format(git_path + '/public/*'))
