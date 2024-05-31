import React, { useState } from 'react';
import Button from './Button';
import InputBox from './InputBox';
import styled from 'styled-components';

const Li = styled.li`
    font-size: 30px;
    display: inline-block;
`;

function Container(props) {
    const [inputValue, setInputValue] = useState('');
    const [items, setItems] = useState([]);
    const [isEditing, setIsEditing] = useState(null);
    const [editValue, setEditValue] = useState('');

    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleEditChange = (e) => {
        setEditValue(e.target.value);
    };

    const addItem = () => {
        if (inputValue) {
            setItems([...items, inputValue]);
            setInputValue('');
        }
    };

    const deleteItem = (index) => {
        setItems(items.filter((_, i) => i !== index));
    };

    const startEditing = (index) => {
        setIsEditing(index);
        setEditValue(items[index]);
    };

    const saveEdit = (index) => {
        if (editValue) {
            const updatedItems = [...items];
            updatedItems[index] = editValue;
            setItems(updatedItems);
            setIsEditing(null);
        }
    };

    console.log(items);
    return (
        <>
            <h1>To Do List</h1>
            <InputBox value={inputValue} onChange={handleInputChange} />
            <Button btnName="추가하기" clickEffect={addItem} />

            <ul>
                {items.map((item, index) => (
                    <Li key={index}>
                        {isEditing === index ? (
                            <>
                                <input type="text" value={editValue} onChange={handleEditChange} />
                                <Button btnName="저장하기" clickEffect={() => saveEdit(index)} />
                            </>
                        ) : (
                            <>
                                {index + 1}. {item}
                                <Button btnName="수정하기" clickEffect={() => startEditing(index)} />
                                <Button btnName="삭제하기" clickEffect={() => deleteItem(index)} />
                            </>
                        )}
                    </Li>
                ))}
            </ul>
        </>
    );
}

export default Container;
