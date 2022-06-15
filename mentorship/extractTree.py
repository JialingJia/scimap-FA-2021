import json
from random import sample

with open("data/menteeadjacentlist.json", 'r', encoding='UTF-8') as f:
    mentee_dict = json.load(f)

with open("data/mentoradjacentlist.json", 'r', encoding='UTF-8') as f:
    mentor_dict = json.load(f)

with open("data/researcherGender1.json", 'r', encoding='UTF-8') as f:
    researcher_dict = json.load(f)

root = 3

output_list = []

gender = ['man', 'woman', 'unknown']
gender_color = ['blue', 'red', 'grey']
research_fields = ['neuro', 'physics', 'psych', 'chemistry', 'fly', 'evol', 'anatomy', 'hist', 'mich', 'math', 'ling', 'phil', 'anthropology', 'polisci', 'dev', 'cellbio', 'compbio', 'animalscience', 'meteorology', 'biomech', 'mareco', 'theology', 'behavior', 'econ', 'advert', 'tereco', 'idtree', 'plantbio', 'etree', 'csd', 'physiology', 'sts', 'pombe', 'telo', 'astrobiology', 'primate', 'bone', 'fluids', 'ssib', 'epidemiology', 'educ', 'plantsys', 'alzh', 'computerscience', 'genetics', 'writingstudies', 'npath', 'astronomy', 'mycology', 'geoscience', 'music', 'sociology', 'law', 'robotics', 'oceanography', 'bme', 'thee', 'crystallography', 'phtree', 'microbiology',
                   'cellgenetherapy', 'neurooncology', 'hypnosis', 'appliedphys', 'bronchopulmonology', 'geography', 'musictherapy', 'pedsurgeons', 'environment', 'literature', 'orgcommunication', 'publichealth', 'stemcell', 'nursing', 'division20', 'socialpsych', 'business', 'marinemammalscience', 'bioethics', 'architecture', 'hdfs', 'cityplanning', 'ntrauma', 'publicpolicy', 'psyphys', 'plasticsurgery', 'division45', 'phycology', 'neurosurgery', 'nonprofit', 'structuralbiology', 'imaging', 'orientalstudies', 'uncw', 'ecotox', 'vision', 'medphysradonc', 'angiogenesis', 'mis', 'chronobiology', 'nutrition', 'womenshealth', 'grouprelations', 'surgicalcriticalcare', 'materials']
research_fields_colors = ['#F3E09A', '#573470', '#3CDE38', '#B0313D', '#7A732A', '#64E1BF', '#1A09CC', '#68A839', '#AA96EB', '#8F3CCC', '#DE12F5', '#835A23', '#583996', '#77E823', '#8365C7', '#60A09F', '#7F5D2B', '#045C3D', '#8E3669', '#D73E6F', '#87BEEB', '#1EC5F6', '#F0D9C7', '#BCA5D6', '#4B3794', '#530283', '#D16086', '#99EF90', '#007235', '#91CF72', '#2AFB8B', '#3008A0', '#73E7CB', '#8D75BF', '#6C8263', '#0A4A91', '#B33A7B', '#145C2A', '#40B44E', '#D74666', '#A3EA27', '#5223F3', '#27DD2D', '#10887E', '#6629E2', '#168998', '#8E9E69', '#24752C', '#7721F3', '#2E7893', '#BD117E',
                          '#AC9CED', '#3AE12E', '#4CD609', '#5F4D80', '#A53F58', '#241CF0', '#E88C22', '#CD6594', '#65B9CA', '#82F0A2', '#97C7EA', '#A62A86', '#EB078A', '#C1C499', '#A2F1D8', '#9BB940', '#2290B9', '#B719D0', '#6FA335', '#72F560', '#CD357F', '#300649', '#66915E', '#17C84D', '#9A2345', '#70B59D', '#887BF1', '#CA3456', '#3F7841', '#ECF990', '#D64184', '#F6F226', '#A944FF', '#E033D7', '#C0260C', '#5E45E2', '#F1F0B9', '#DC69F1', '#FC835C', '#90C322', '#E808DE', '#EBCD2C', '#898801', '#A65058', '#549A64', '#9A910A', '#5100FD', '#3628BD', '#0F2A2A', '#6F8209', '#AAFA5F', '#E66052', '#9E21F3', '#3DFABE']
existed_id = []


def getAllResearchers(field):
    candidateList = []
    for i in researcher_dict:
        if 'ResearchArea' in i and field in i['ResearchArea'].split(","):
            candidateList.append(i)
    # researcherID = candidateList[0]['index']
    max_num = 0

    # for i in candidateList:
    #     if max_num > len(mentee_dict[i['index']]):
    #         researcherID = i['index']
    #         max_num = len(mentee_dict[i['index']])

    return candidateList


def getAllResearchersWithoutMentors(field):
    researchers_information = getAllResearchers(field)
    researchers = []
    for i in researchers_information:
        researchers.append(i['index'])

    researchersWithoutMentors = []

    for i in researchers:
        tmp_index = i
        tmp_list = mentor_dict[tmp_index]
        flag = True
        for j in tmp_list:
            if j in researchers:
                flag = False
                break
        if flag == True:
            researchersWithoutMentors.append(i)
    return researchersWithoutMentors


def getDict(id, current_layer, target, target_field=''):
    if (current_layer == target):
        new_dict = {}
        new_dict['name'] = researcher_dict[id]['name']
        # new_dict['id'] = id
        new_dict['gender'] = researcher_dict[id]['Gender']
        new_dict['gender_color'] = gender_color[gender.index(
            new_dict['gender'])]
        new_dict['researcharea'] = researcher_dict[id]['ResearchArea'].split(
            ",")
        # new_dict['researcharea_color'] = research_fields_colors[research_fields.index(new_dict['researcharea'])]
        mentee_list = set(mentee_dict[id])
        children_list = []
        for i in mentee_list:
            # if (target_field != ''):
            #     if (i in existed_id or target_field not in researcher_dict[i]['ResearchArea'].split(",")):
            #         continue
            # else:
            #     if (i in existed_id):
            #         continue
            if (i in existed_id):
                continue
            tmp_dict = {}
            tmp_dict['name'] = researcher_dict[i]['name']
            # tmp_dict['id'] = id
            tmp_dict['gender'] = researcher_dict[i]['Gender']
            tmp_dict['gender_color'] = gender_color[gender.index(
                tmp_dict['gender'])]
            tmp_dict['researcharea'] = researcher_dict[i]['ResearchArea'].split(
                ",")
            # tmp_dict['researcharea_color'] = research_fields_colors[research_fields.index(tmp_dict['researcharea'])]
            # tmp_dict['children'] = []
            if (tmp_dict['gender'] == 'woman'):
                children_list.insert(0, tmp_dict)
            else:
                children_list.append(tmp_dict)
            existed_id.append(i)
        if children_list != []:
            new_dict['children'] = children_list
        new_dict['children_num'] = 0
        return new_dict
    else:
        new_dict = {}
        existed_id.append(id)
        new_dict['name'] = researcher_dict[id]['name']
        # new_dict['id'] = id
        new_dict['gender'] = researcher_dict[id]['Gender']
        new_dict['gender_color'] = gender_color[gender.index(
            new_dict['gender'])]
        new_dict['researcharea'] = researcher_dict[id]['ResearchArea'].split(
            ",")
        # new_dict['researcharea_color'] = research_fields_colors[research_fields.index(new_dict['researcharea'])]
        new_dict['children_num'] = 0
        mentee_list = set(mentee_dict[id])
        children_list = []
        for i in mentee_list:
            # if (i in existed_id or target_field not in researcher_dict[i]['ResearchArea'].split(",")):
            #     continue
            if (i in existed_id):
                continue
            tmp_dict = getDict(i, current_layer+1, target, target_field)
            if (tmp_dict['gender'] == 'woman'):
                children_list.insert(0, tmp_dict)
            else:
                children_list.append(tmp_dict)
            existed_id.append(i)
        if children_list != []:
            new_dict['children'] = children_list
    return new_dict


def getDepth(id):
    if 'children' not in id or len(id['children']) == 0:
        return 0
    else:
        depth_list = []
        for i in id['children']:
            depth_list.append(getDepth(i))
        return max(depth_list) + 1


def postorder(id):
    if 'children' not in id:
        id['children_num'] = 0
        return 0
    else:
        total_num = 0
        for tmp in id['children']:
            total_num += postorder(tmp) + 1
        id['children_num'] = total_num
        return total_num
