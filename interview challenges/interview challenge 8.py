1. Design a web application that is a Twitter clone. Describe the URLs and what each URL does like the ToDo App exercise. The app should be able to post a message, follow other users, view my list of messages and the people I follow, and view a list of messages from another user.

This is a non-coding challenging. You only need to create the specification of what you want built. Imagine your the manager and you need to describe what needs to be built to other developers.

1. Spoken.com- This is the main page that users see as soon as they log in. On this page they will be able to see all activity of the people that they follow and get real time updates from everyone that they follow. They will also be able to "speak" their mind and thoughts visible by all their followers.

2. spoken/add- This page will allow users to add friends/follow their friends that can be imported from their adressbook/facebook list of already existing friends. This page will also display a suggestions page where some people that share mutual connections will be displayed for your chance to "speak" to them- ,add them to your follow list. It will also generate a table based on simmilar interests that will allow you to follow them as well.

3. spoken/messages- This page users will be able to create messages to privately send/receive to and from other spoken members. They will also be able to form group private messages here where they can share links/images/videos whatever they want no matter how big or small the file is.

Question 2
------------

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print "sum(%s)=%s" % (partial, target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])




if __name__ == "__main__":
    subset_sum([3,9,8,4,5,7,10],12)
