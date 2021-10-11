class DataObtainer:

    def data_userinfo_organized(self, data):
        # User information
        get_screen_name = data['user']['screen_name']
        get_user_id = data['user']['id']
        get_user_id_str = data['user']['id_str']
        is_truncated = data['truncated']

        # Append in dictionary
        user_information = {"User Name": get_screen_name,
                            "User ID": get_user_id,
                            "User ID Str": get_user_id_str,
                            "Is Truncated": is_truncated}

        # print("User Information: ", user_information)

        return user_information

    def data_statusinfo_organized(self, data):
        # Status Information
        get_status_text = data['text']

        # exceptional case
        get_hashtag_from_status = data['entities']['hashtags']  # the hashtag format (lower, upper, etc) writes by user
        # =======
        get_status_id = data['id']  # type is int
        get_status_id_str = data['id_str']

        # Append in dictionary
        status_information = {"Status Text": get_status_text,
                              "Status ID": get_status_id,
                              "Status ID Str": get_status_id_str,
                              "Status Hashtag Typed": get_hashtag_from_status}

        # print("Status Information: ", status_information)

        return status_information

    def data_statussituation_organized(self, data):
        # Status situation
        get_status_language = data['lang']
        is_status_retweeted = data['retweeted']
        reply_to_status_id = data['in_reply_to_status_id']
        reply_to_status_id_str = data['in_reply_to_status_id_str']
        reply_to_user_id = data['in_reply_to_user_id']
        in_reply_to_user_id_str = data['in_reply_to_user_id_str']
        in_reply_to_screen_name = data['in_reply_to_screen_name']

        # Append in dictionary
        status_situation = {"Status Language": get_status_language,
                            "Is retweeted": is_status_retweeted,
                            "Reply Status ID": reply_to_status_id,
                            "Reply Status ID Str": reply_to_status_id_str,
                            "Reply User ID": reply_to_user_id,
                            "Reply User ID Str": in_reply_to_user_id_str,
                            "Reply Screen Name": in_reply_to_screen_name, }

        # print("Status Situation: ", status_situation)

        return status_situation

    # This function returns a dictionary with a str in value
    def status_hashtag_typed(self, dict_or_list):

            index = dict_or_list[0]
            del index['indices']
            status_hashtag = index['text']

            return status_hashtag

# Testes
# d = DataObtainer()
# print(d.data_userinfo_organized(data=data_dict))
# print(d.data_statusinfo_organized(data=data_dict))
# print(d.data_statussituation_organized(data=data_dict))
