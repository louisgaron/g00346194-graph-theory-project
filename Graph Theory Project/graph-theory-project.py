import os
import pickle
import PySimpleGUI as sg

#This is the GUI layout that should be seen by the user in the screen
class Gui:
    def __init__(self):
        self.layout = [[sg.Text('Search File', size=(10,1)), 
                        sg.Input(size=(45,1), focus=True, key="SEARCHWORD"), 
                        sg.Radio('Contains', group_id='choice', key="CONTAINS"), 
                        sg.Radio('StartsWith', group_id='choice', key="STARTSWITH"), 
                        sg.Radio('EndsWith', group_id='choice', key="ENDSWITH")], 
                        [sg.Text('Root Path', size=(10,1)), 
                        sg.Input('C:/ ', size=(45,1), key="PATH"), 
                        sg.FolderBrowse('Browse'), 
                        sg.Button('Re-Index', size=(10,1), key="__INDEX__"), s
                        sg.Button('Search', size=(10,1), bind_return_key=True, key="SEARCH")],
                        [sg.Output(size=(100,30))]]
                        
        self.window - sg.Window('Text File Search').Layout(self.layout)

class SearchEngine:
    def __init__(self):
        self.file_index = []
        self.result = []
        self.matches = 0
        self.records = 0

        def create_new_index(self, values):
            ''' create a new index and save to file '''
            root_path = values['PATH']
            self.file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]

            #save to file
            with open('file_index.pk1', 'wb') as f:
                pickle.dump(self.file_index, f)

        def load_existing_index(self):
            ''' load existing index '''
            try:
                with open('file_index.pk1', 'wb') as f:
                    self.file_index - pickle.load(f)
            except:
                self.file_index = []

        def search(self, values):
            ''' search for term based on search type '''
            
            #reset variables
            self.results.clear()
            self.matches = 0
            self.records = 0
            searchWord = values['SEARCHWORD']

            #performs searches
            for path, files in self.file_index:
                for file in files:
                    self.records +=1
                    if (values['CONTAINS'] and term.lower() in file.lower() or
                        values['STARTSWITH'] and file.lower().startswith(term.lower()) or
                        values['ENDSWITH'] and file.lower().endswith(term.lower())):

                        result = path.replace('\\', '/') + '/' + file
                        self.results.append(result)
                        self.matches +=1
                    else:
                        continue

            #saves the search results
            with open('search_results.txt', 'w') as f:
                for row in self.results:
                    f.write(row + '\n')

#This test is built to count if the searched word matches any files, how many files or if it didn't match any files 
def test1():
    s = SearchEngine()
    s.load_existing_index()
    s.search('gecko')

    print()
    print('There were [:,d} matches our of [:,d} records searched.', format(s.matches, s.records))
    print()
    print('Following matches: \n')
    for match in s.result:
        print(match)


#This tests the word put in the search box if the case is true or false in each button meaning: If the filename contains that word or starts with or ends with it will state in all different cases.
def test2():
    g = Gui()
   while True:
       event, values = g.window.Read()
       print(event,values)

def main():
    g = Gui()
    s = SearchEngine()
    s.load_existing_index()

    while True:
        event, values = g.window.Read()

        if event is None:
            break
        if event = '__INDEX__':
            s.create_new_index(values)

            print()
            print('New Index Created')
            print()

            if event == 'SEARCH':
                s.search(values)

                #print results
                print()
                for result in s.results():
                    print(result)

                print()
                print('There were [:,d} matches our of [:,d} records searched.', format(s.matches, s.records))
                print()
                print('Following matches: \n')
                print('File is Saved')
    